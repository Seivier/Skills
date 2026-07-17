#!/usr/bin/env python3
"""
Detecta los capitulos de un markdown de pandoc (generado a partir de un EPUB)
e imprime un manifiesto en JSON -- NO escribe archivos por capitulo a disco.

Uso:
    python split_chapters.py <entrada.md> [--level N]

Por defecto intenta detectar encabezados H1 (#). Si eso da menos de 2
capitulos, prueba H2 (##). Usa --level para forzar uno de los dos si el
auto-detect elige mal (pandoc no siempre deja los encabezados limpios).

Salida (stdout), un JSON con esta forma:
{
  "level": 1,
  "chapters": [
    {"title": "Principios SOLID en la practica", "start_line": 1, "end_line": 18},
    {"title": "Patrones creacionales...", "start_line": 19, "end_line": 40}
  ]
}

start_line/end_line son 1-indexados e inclusivos, pensados para usarse con
view_file (StartLine/EndLine) o para extraer el texto del capitulo directamente
en Python si se esta orquestando desde un script.
"""
import argparse
import json
import re
import sys


def find_chapters_by_level(lines, level):
    pattern = re.compile(r"^" + ("#" * level) + r"\s+(.+)$")
    starts = []
    for i, line in enumerate(lines):
        m = pattern.match(line)
        if m:
            starts.append((i, m.group(1).strip()))
    if len(starts) < 2:
        return None
    chapters = []
    for idx, (start_idx, title) in enumerate(starts):
        if idx + 1 < len(starts):
            end_idx = starts[idx + 1][0] - 1
        else:
            end_idx = len(lines) - 1
        chapters.append({
            "title": title,
            "start_line": start_idx + 1,
            "end_line": end_idx + 1,
        })
    return chapters


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input_md")
    ap.add_argument(
        "--level",
        type=int,
        default=0,
        choices=[0, 1, 2],
        help="Nivel de encabezado a usar (1=H1, 2=H2). 0 = auto-detectar (default).",
    )
    args = ap.parse_args()

    try:
        with open(args.input_md, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

    levels_to_try = [args.level] if args.level else [1, 2]
    chapters = None
    used_level = None
    for lvl in levels_to_try:
        chapters = find_chapters_by_level(lines, lvl)
        if chapters:
            used_level = lvl
            break

    if not chapters:
        print(
            "No se pudieron detectar capitulos con encabezados H1 o H2.\n"
            "Puede que este pandoc en particular no haya dejado encabezados limpios.\n"
            "Revisa el markdown manualmente (view_file) y arma el manifiesto a mano, o especifica --level.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(json.dumps({"level": used_level, "chapters": chapters}, ensure_ascii=False, indent=2))
    print("\n" + str(len(chapters)) + " capitulos detectados usando H" + str(used_level) + ".", file=sys.stderr)


if __name__ == "__main__":
    main()
