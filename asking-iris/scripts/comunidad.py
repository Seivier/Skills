#!/usr/bin/env python3
"""Lee y edita references/comunidad.json -- la reputación de los usuarios
de community.intersystems.com cuyos aportes se citan en los libros de esta
skill.

El JSON es la fuente de verdad (preciso, editable a mano si hace falta);
este script da una vista concisa para lectura y comandos para no tener que
editar el JSON manualmente en el caso comun. Toda salida de lectura (show,
buscar) se presenta en tablas -- una para la reputación agregada y otra
para el detalle de propuestas -- así "¿cuál es la reputación de X?" y
"¿qué propuestas hizo X?" siempre se leen con el mismo formato.

Comandos:
    show   [--usuario SLUG] [--solo-tabla]   ver reputación (tabla + detalle)
    buscar <query>                            localizar un aporte por texto/URL/capítulo
    add    --usuario ... --propuesta ... --url ... --veredicto ...
    update --url ... --veredicto ...          actualizar el veredicto de un aporte existente
    marcar --usuario ... --nivel ...          marcar/desmarcar un usuario como oficial o de confianza
    add-nota --texto ...                      registrar una lección operativa puntual

Uso: python3 comunidad.py <comando> --help  para el detalle de cada uno.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "references" / "comunidad.json"
VEREDICTOS = ["confirmada", "refutada", "no_aplico", "sin_verificar"]
ICONOS = {"confirmada": "✅", "refutada": "❌", "no_aplico": "➖", "sin_verificar": "❔"}
NIVELES = ["normal", "confianza", "oficial"]
ICONOS_NIVEL = {"confianza": "⭐", "oficial": "🏛️"}


def cargar():
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def guardar(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def slugify_desde_perfil(perfil):
    return perfil.rstrip("/").rsplit("/user/", 1)[-1]


def truncar(texto, n=90):
    texto = str(texto)
    return texto if len(texto) <= n else texto[: n - 1].rstrip() + "…"


def nombre_con_nivel(u):
    """Nombre para mostrar en tablas, con el ícono de nivel de confianza si aplica."""
    icono = ICONOS_NIVEL.get(u.get("nivel", "normal"))
    return f"{icono} {u['nombre']}" if icono else u["nombre"]


def render_table(headers, rows):
    """Tabla markdown con columnas alineadas al contenido más ancho de cada una."""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    def fmt(cells):
        return "| " + " | ".join(str(c).ljust(widths[i]) for i, c in enumerate(cells)) + " |"

    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    return "\n".join([fmt(headers), sep] + [fmt(r) for r in rows])


def tabla_conteos(usuarios):
    """Tabla de reputación agregada -- responde '¿cuál es la reputación de X?'."""
    if not usuarios:
        return "(sin usuarios registrados todavía)"
    rows = []
    for u in usuarios:
        conteo = {v: 0 for v in VEREDICTOS}
        for p in u["propuestas"]:
            conteo[p["veredicto"]] += 1
        nivel = u.get("nivel", "normal")
        etiqueta_nivel = f"{ICONOS_NIVEL[nivel]} {nivel}" if nivel != "normal" else "-"
        rows.append(
            [u["nombre"], etiqueta_nivel, conteo["confirmada"], conteo["refutada"], conteo["no_aplico"], conteo["sin_verificar"]]
        )
    return render_table(["Usuario", "Nivel", "Confirmadas", "Refutadas", "No aplicó", "Sin verificar"], rows)


def tabla_propuestas(entradas, incluir_usuario=True):
    """Tabla de detalle -- responde '¿qué propuestas hizo X?'.

    entradas: lista de (nombre_dueño, propuesta_dict).
    Devuelve (tabla_str, fuentes) -- fuentes es la lista "[n] url -- nota (fecha)"
    referenciada por la columna Fuente, para no repetir URLs largas en cada fila.
    """
    if not entradas:
        return "(sin propuestas)", []
    headers = (["Usuario"] if incluir_usuario else []) + ["Veredicto", "Propuesta", "Usado en", "Fuente"]
    rows, fuentes = [], []
    for i, (dueño, p) in enumerate(entradas, start=1):
        fila = ([dueño] if incluir_usuario else []) + [
            f"{ICONOS.get(p['veredicto'], '?')} {p['veredicto']}",
            truncar(p["propuesta"]),
            truncar(p.get("usado_en") or "-", 40),
            f"[{i}]",
        ]
        rows.append(fila)
        detalle = p["url"]
        if p.get("nota"):
            detalle += f" -- {p['nota']}"
        if p.get("fecha"):
            detalle += f" ({p['fecha']})"
        fuentes.append(f"[{i}] {detalle}")
    return render_table(headers, rows), fuentes


def imprimir_fuentes(fuentes):
    if fuentes:
        print("Fuentes:")
        for f in fuentes:
            print(f"  {f}")


def cmd_show(args):
    data = cargar()
    usuarios = data["usuarios"]
    if args.usuario:
        usuarios = [u for u in usuarios if u["slug"] == args.usuario or u["nombre"] == args.usuario]
        if not usuarios:
            print(f"No hay usuario con slug/nombre '{args.usuario}'.", file=sys.stderr)
            return 1

    print("=== Reputación de la comunidad (community.intersystems.com) ===\n")
    print(tabla_conteos(usuarios))

    if args.solo_tabla:
        return 0

    for u in usuarios:
        print(f"\n--- Propuestas de {nombre_con_nivel(u)} ({u['perfil']}) ---")
        nivel = u.get("nivel", "normal")
        if nivel != "normal":
            detalle_nivel = f"Nivel: {ICONOS_NIVEL[nivel]} {nivel}"
            if u.get("nivel_nota"):
                detalle_nivel += f" -- {u['nivel_nota']}"
            if u.get("nivel_fecha"):
                detalle_nivel += f" (marcado el {u['nivel_fecha']})"
            print(detalle_nivel)
        tabla, fuentes = tabla_propuestas([(u["nombre"], p) for p in u["propuestas"]], incluir_usuario=False)
        print(tabla)
        imprimir_fuentes(fuentes)

    if not args.usuario:
        pid = data.get("por_identificar", {})
        if pid.get("aportes"):
            print(f"\n--- Por identificar ({len(pid['aportes'])}) ---")
            print(pid.get("nota", ""))
            tabla, fuentes = tabla_propuestas(
                [("(por identificar)", p) for p in pid["aportes"]], incluir_usuario=False
            )
            print(tabla)
            imprimir_fuentes(fuentes)

        if data.get("notas"):
            print("\n--- Notas de incidentes ---")
            print(render_table(["Fecha", "Nota"], [[n["fecha"], truncar(n["texto"], 110)] for n in data["notas"]]))
            print("(texto completo en references/comunidad.json -> notas)")

    return 0


def cmd_buscar(args):
    data = cargar()
    query = args.query.lower()
    encontrados = []

    for u in data["usuarios"]:
        for p in u["propuestas"]:
            campos = " ".join(str(p.get(c, "")) for c in ("propuesta", "url", "usado_en", "nota"))
            if query in campos.lower() or query in u["nombre"].lower() or query in u["slug"].lower():
                encontrados.append((nombre_con_nivel(u), p))

    for p in data.get("por_identificar", {}).get("aportes", []):
        campos = " ".join(str(p.get(c, "")) for c in ("propuesta", "url", "usado_en", "nota"))
        if query in campos.lower():
            encontrados.append(("(por identificar)", p))

    if not encontrados:
        print(f"Sin resultados para '{args.query}'.")
        return 1

    print(f"{len(encontrados)} resultado(s) para '{args.query}':\n")
    tabla, fuentes = tabla_propuestas(encontrados, incluir_usuario=True)
    print(tabla)
    imprimir_fuentes(fuentes)
    return 0


def cmd_add(args):
    data = cargar()
    slug = args.slug or (slugify_desde_perfil(args.perfil) if args.perfil else args.usuario)
    usuario = next((u for u in data["usuarios"] if u["slug"] == slug), None)
    if usuario is None:
        usuario = {
            "slug": slug,
            "nombre": args.usuario,
            "perfil": args.perfil or "",
            "propuestas": [],
        }
        data["usuarios"].append(usuario)

    nueva = {
        "propuesta": args.propuesta,
        "url": args.url,
        "usado_en": args.usado_en,
        "veredicto": args.veredicto,
        "nota": args.nota,
        "fecha": args.fecha or datetime.date.today().isoformat(),
    }
    usuario["propuestas"].append(nueva)
    guardar(data)
    print(f"Agregado a {usuario['nombre']} ({slug}):")
    tabla, fuentes = tabla_propuestas([(usuario["nombre"], nueva)], incluir_usuario=False)
    print(tabla)
    imprimir_fuentes(fuentes)
    return 0


def cmd_update(args):
    data = cargar()
    candidatos = []
    for u in data["usuarios"]:
        for p in u["propuestas"]:
            if args.url.lower() in p["url"].lower():
                candidatos.append((u, p))

    if not candidatos:
        print(f"Ningún aporte coincide con la URL '{args.url}'.", file=sys.stderr)
        return 1
    if len(candidatos) > 1:
        print(f"'{args.url}' coincide con {len(candidatos)} aportes -- sé más específico:", file=sys.stderr)
        for u, p in candidatos:
            print(f"  - {u['nombre']}: {p['propuesta'][:80]}", file=sys.stderr)
        return 1

    u, p = candidatos[0]
    if args.veredicto:
        p["veredicto"] = args.veredicto
    if args.nota is not None:
        p["nota"] = args.nota
    if args.usado_en is not None:
        p["usado_en"] = args.usado_en
    if args.fecha:
        p["fecha"] = args.fecha
    elif args.veredicto:
        p["fecha"] = datetime.date.today().isoformat()

    guardar(data)
    print(f"Actualizado -- {u['nombre']}:")
    tabla, fuentes = tabla_propuestas([(u["nombre"], p)], incluir_usuario=False)
    print(tabla)
    imprimir_fuentes(fuentes)
    return 0


def cmd_marcar(args):
    data = cargar()
    slug = args.slug or (slugify_desde_perfil(args.perfil) if args.perfil else args.usuario)
    usuario = next((u for u in data["usuarios"] if u["slug"] == slug or u["nombre"] == args.usuario), None)
    if usuario is None:
        usuario = {
            "slug": slug,
            "nombre": args.usuario,
            "perfil": args.perfil or "",
            "propuestas": [],
        }
        data["usuarios"].append(usuario)

    if args.nivel == "normal":
        usuario.pop("nivel", None)
        usuario.pop("nivel_nota", None)
        usuario.pop("nivel_fecha", None)
    else:
        usuario["nivel"] = args.nivel
        usuario["nivel_nota"] = args.nota
        usuario["nivel_fecha"] = args.fecha or datetime.date.today().isoformat()

    guardar(data)
    if args.nivel == "normal":
        print(f"{usuario['nombre']} ({usuario['slug']}) desmarcado -- vuelve a nivel normal.")
    else:
        print(f"{usuario['nombre']} ({usuario['slug']}) marcado como {ICONOS_NIVEL[args.nivel]} {args.nivel}.")
        if args.nota:
            print(f"Nota: {args.nota}")
    return 0


def cmd_add_nota(args):
    data = cargar()
    data.setdefault("notas", []).append(
        {"fecha": args.fecha or datetime.date.today().isoformat(), "texto": args.texto}
    )
    guardar(data)
    print("Nota agregada.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="comando", required=True)

    p_show = sub.add_parser("show", help="ver reputación (tabla + detalle)")
    p_show.add_argument("--usuario", help="filtrar por slug o nombre de un usuario")
    p_show.add_argument("--solo-tabla", action="store_true", help="solo la tabla de conteos, sin el detalle por aporte")
    p_show.set_defaults(func=cmd_show)

    p_buscar = sub.add_parser("buscar", help="localizar un aporte por autor, URL, texto o capítulo")
    p_buscar.add_argument("query")
    p_buscar.set_defaults(func=cmd_buscar)

    p_add = sub.add_parser("add", help="registrar un aporte nuevo")
    p_add.add_argument("--usuario", required=True, help="nombre mostrado del usuario")
    p_add.add_argument("--slug", help="slug real del perfil (si no se pasa, se deriva de --perfil o de --usuario)")
    p_add.add_argument("--perfil", help="URL del perfil de community.intersystems.com")
    p_add.add_argument("--propuesta", required=True)
    p_add.add_argument("--url", required=True, help="URL del hilo")
    p_add.add_argument("--usado-en", dest="usado_en", help="capítulo del libro donde se usó")
    p_add.add_argument("--veredicto", required=True, choices=VEREDICTOS)
    p_add.add_argument("--nota", help="justificación breve del veredicto")
    p_add.add_argument("--fecha", help="AAAA-MM-DD (default: hoy)")
    p_add.set_defaults(func=cmd_add)

    p_update = sub.add_parser("update", help="actualizar el veredicto de un aporte existente (localizado por URL)")
    p_update.add_argument("--url", required=True, help="URL (o parte de ella) del aporte a actualizar")
    p_update.add_argument("--veredicto", choices=VEREDICTOS)
    p_update.add_argument("--nota", help="nueva justificación (usa '' para borrarla)")
    p_update.add_argument("--usado-en", dest="usado_en", help="nuevo capítulo donde se usó")
    p_update.add_argument("--fecha", help="AAAA-MM-DD (default: hoy, si cambia el veredicto)")
    p_update.set_defaults(func=cmd_update)

    p_marcar = sub.add_parser(
        "marcar", help="marcar (u desmarcar) un usuario como oficial o de confianza"
    )
    p_marcar.add_argument("--usuario", required=True, help="slug o nombre mostrado del usuario")
    p_marcar.add_argument("--slug", help="slug real del perfil (si no se pasa, se deriva de --perfil o de --usuario)")
    p_marcar.add_argument("--perfil", help="URL del perfil de community.intersystems.com (solo si el usuario es nuevo)")
    p_marcar.add_argument(
        "--nivel",
        required=True,
        choices=NIVELES,
        help="oficial (p. ej. empleado/moderador de InterSystems), confianza (track record propio validado), normal (desmarcar)",
    )
    p_marcar.add_argument("--nota", help="justificación de por qué se marca así (por qué se confía en este usuario)")
    p_marcar.add_argument("--fecha", help="AAAA-MM-DD (default: hoy)")
    p_marcar.set_defaults(func=cmd_marcar)

    p_nota = sub.add_parser("add-nota", help="registrar una lección operativa puntual (no es reputación de un usuario)")
    p_nota.add_argument("--texto", required=True)
    p_nota.add_argument("--fecha", help="AAAA-MM-DD (default: hoy)")
    p_nota.set_defaults(func=cmd_add_nota)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
