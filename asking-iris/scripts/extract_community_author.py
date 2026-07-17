#!/usr/bin/env python3
"""Extrae el autor de la pregunta y el autor de cada respuesta de un hilo
de community.intersystems.com, usando curl con un User-Agent de navegador
normal (WebFetch devuelve 403 en este dominio; curl con el mismo HTML publico
no).

Uso exclusivo: identificar QUIEN dijo que. No reemplaza leer el contenido
del hilo -- para eso segui usando WebFetch/WebSearch como siempre. Este
script existe porque un resumen de WebSearch tiende a mezclar "quien
pregunto" con "quien respondio", que en el HTML real son nodos DOM
distintos (node__author vs comment__author).

Uso:
    python3 extract_community_author.py <url-del-hilo>

Salida: JSON con question_author y una lista de comments (autor, fecha,
a quien responde si aplica).
"""
import json
import re
import subprocess
import sys
from urllib.parse import unquote

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)

USER_LINK_RE = r'https://community\.intersystems\.com/user/[^"]+'


def fetch(url):
    result = subprocess.run(
        ["curl", "-s", "-A", UA, url],
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    return result.stdout


def user_slug(profile_url):
    """El slug real del usuario (path tras /user/), no el nombre mostrado
    -- el nombre visible puede no coincidir con el slug (p. ej. "Kurro
    Lopez" en pantalla, pero /user/francisco-l%C3%B3pez1549 en el href)."""
    path = profile_url.split("/user/", 1)[-1]
    return unquote(path.rstrip("/"))


def unescape(s):
    return (
        s.replace("&amp;", "&")
        .replace("&nbsp;", " ")
        .replace("&quot;", '"')
        .replace("&#039;", "'")
        .strip()
    )


def extract(html):
    question = None
    m = re.search(
        r'<a href="(' + USER_LINK_RE + r')"><span class="node__author">([^<]+)</span></a>',
        html,
    )
    if m:
        question = {
            "profile_url": m.group(1),
            "user": user_slug(m.group(1)),
            "name": unescape(m.group(2)),
        }

    comment_re = re.compile(
        r'<a href="(' + USER_LINK_RE + r')"><span class="comment__author">([^<]+)</span></a>'
    )
    reply_re = re.compile(
        r'<small itemprop="dateCreated">'
        r'<span class="commentreplyed"[^>]*>\s*([^<]+?)(?:\s+to\s+([^<]+))?</span></small>'
    )

    reply_matches = list(reply_re.finditer(html))
    comments = []
    for cm in comment_re.finditer(html):
        date, reply_to = None, None
        # el bloque de fecha/reply-to de este comentario aparece poco
        # despues del tag de autor en el HTML del tema
        for rm in reply_matches:
            if rm.start() > cm.end() and rm.start() - cm.end() < 400:
                date = unescape(rm.group(1))
                reply_to = unescape(rm.group(2)) if rm.group(2) else None
                break
        comments.append(
            {
                "author": unescape(cm.group(2)),
                "profile_url": cm.group(1),
                "user": user_slug(cm.group(1)),
                "date": date,
                "reply_to": reply_to,
            }
        )

    return {"question_author": question, "comments": comments}


def main():
    if len(sys.argv) != 2:
        print("Uso: extract_community_author.py <url-del-hilo>", file=sys.stderr)
        sys.exit(1)
    url = sys.argv[1]
    data = extract(fetch(url))
    data["url"] = url
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
