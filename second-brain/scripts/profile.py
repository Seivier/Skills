#!/usr/bin/env python3
# DEPRECADO (2026-07-13): reemplazado por el MCP de Notion, ver
# references/notion-portability-design.md y references/notion-portability-plan.md.
# Se conserva sin borrar como referencia histórica; SKILL.md ya no lo invoca.
"""Gestor del perfil personal — única vía autorizada para tocar los datos.

El perfil vive en ~/.claude/second-brain/profile.json y es, de punta a punta,
UN ÁRBOL DE NODOS. No hay distinción estructural entre "eje" y "subeje": todo
es el mismo tipo de nodo, con el mismo shape, a cualquier profundidad:

    { "name": str, "desc": str|null, "info": str|null, "childs": [nodo, ...] }

- "name": identificador del nodo (único entre sus hermanos).
- "desc": resumen de una línea de qué contiene este nodo o su subárbol.
- "info": el contenido real del nodo, SIEMPRE texto plano (o null si el nodo
  es puramente organizador y no tiene contenido propio). Nada de JSON anidado
  dentro de info — si necesitas estructura, esa es la señal de que el dato
  debería vivir en childs, no embebido como objeto dentro de info.
- "childs": lista de nodos hijos, mismo shape recursivamente. Un nodo sin
  hijos es un nodo terminal (hoja) — ahí suele vivir la info atómica real.
  Un nodo puede tener info Y childs a la vez (resumen propio + detalle
  ramificado debajo).

Regla de ramificación: cuando el texto de "info" crece demasiado o empieza a
mezclar temas distintos, se divide — cada sub-tema pasa a ser un child propio
con su info acotada, y el padre se queda solo con lo transversal (o con info
null si ya no le queda nada propio). No ramifiques por anticipado solo porque
un dato "tiene varias partes"; ramifica cuando el texto efectivamente ya
pesa o mezcla cosas que conviene poder consultar por separado.

Los 6 ejes de primer nivel (salud, emocional, proyectos, trabajo, academico,
general) son también nodos — son fijos, los define este script (no los inventa
Claude) y son el punto de entrada del árbol de cada tema. Todo lo demás
(qué antes eran campos fijos como "items" o "preferencias_tecnicas", y lo que
antes eran "subejes") son ahora simplemente childs — sin excepciones, sin
campos especiales. Los crea y mantiene el propio Claude (ver SKILL.md sección
2.1 y references/subejes.md para el catálogo).

Las NOTAS son la única excepción a "todo es un nodo del árbol": viven aparte,
como una lista plana con id en el eje raíz (`db[eje]["note"]`), no como un
child más. Son el log crudo de captura — cada una tiene id/fecha/texto. Cuando
una nota se refleja en un nodo estructurado, el `info` de ese nodo puede citar
la nota por id (ej. "... (ver nota salud#5)") para dejar trazabilidad sin
duplicar el texto ni forzarla a vivir dentro del árbol.

Los comandos de lectura NUNCA vuelcan el JSON crudo por defecto — dan vistas
pensadas para navegar el árbol sin leerlo entero:
    tree   -> estructura (nombres + desc, recursivo), sin contenido
    list   -> hijos directos de un nodo (nombres + desc), sin bajar más
    show   -> contenido (desc + info) de UN nodo puntual + nombres de sus hijos
Usa --raw en `show` si de verdad necesitas el JSON literal del nodo (debug).

Uso:
    profile.py tree [eje] [path]
    profile.py list [eje] [path]
    profile.py show <eje> [path] [--raw]
    profile.py set <eje> <path> [--desc "..."] [--info "texto plano"]
    profile.py append <eje> <path> "texto" [--desc "..."]   # agrega una línea fechada al info (texto plano) de un nodo del árbol; lo crea si no existe
    profile.py rm <eje> <path> [--force]                     # elimina un nodo (y su subárbol con --force)
    profile.py note <eje> "texto"               # agrega una nota cruda con id al eje (NO al árbol); imprime el id para citarlo
    profile.py notas <eje>                      # lista las notas del eje con su id (barato, no vía de consulta habitual)
    profile.py rm-nota <eje> <id>               # elimina una nota por id
    profile.py insights                        # lista conclusiones propias sobre el usuario
    profile.py insight "texto"                 # agrega una conclusión propia (no dicha por el usuario)
    profile.py rm-insight <indice>
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

BASE = Path.home() / ".claude" / "second-brain"
DATA = BASE / "profile.json"

SECCIONES = ["salud", "emocional", "proyectos", "trabajo", "academico", "general"]

EJE_DESC = {
    "salud": "Ejercicio, dieta, salud física",
    "emocional": "Motivación, salud psicológica",
    "proyectos": "Proyectos de cualquier tipo (personales, laborales, académicos)",
    "trabajo": "Contexto y preferencias relativas al trabajo",
    "academico": "Tesis, investigación, academia",
    "general": "Todo lo demás, incluidas preferencias técnicas de desarrollo",
}


def now():
    return datetime.now().isoformat(timespec="seconds")


def new_node(name, desc=None, info=None):
    return {"name": name, "desc": desc, "info": info, "childs": []}


def new_eje(name):
    node = new_node(name, EJE_DESC[name])
    node["note"] = []
    return node


def empty():
    return {
        "version": 6,
        "insights": [],
        **{eje: new_eje(eje) for eje in SECCIONES},
    }


def load():
    if not DATA.exists():
        return empty()
    db = json.loads(DATA.read_text())
    db.setdefault("version", 6)
    db.setdefault("insights", [])
    for eje in SECCIONES:
        db.setdefault(eje, new_eje(eje))
        db[eje].setdefault("note", [])
    return db


def save(db):
    BASE.mkdir(parents=True, exist_ok=True)
    tmp = DATA.with_name(DATA.name + ".tmp")
    tmp.write_text(json.dumps(db, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(DATA)


def check_eje_valid(eje):
    if eje not in SECCIONES:
        sys.exit(f"Eje inválido: {eje!r}. Opciones: {', '.join(SECCIONES)}")


def find_child(node, name):
    for c in node["childs"]:
        if c["name"] == name:
            return c
    return None


def resolve_path(db, eje, path, create=False):
    """Devuelve el nodo en <path> (notación de punto) dentro de <eje>."""
    node = db[eje]
    if not path:
        return node
    parts = path.split(".")
    for i, part in enumerate(parts):
        child = find_child(node, part)
        if child is None:
            if not create:
                sys.exit(f"Nodo inexistente: {eje}.{'.'.join(parts[:i + 1])}")
            child = new_node(part)
            node["childs"].append(child)
        node = child
    return node


def resolve_parent(db, eje, path, create=False):
    """Devuelve (nodo_padre, nombre_del_ultimo_tramo) para <path> (>=1 tramo)."""
    parts = path.split(".")
    if len(parts) == 1:
        return db[eje], parts[0]
    parent = resolve_path(db, eje, ".".join(parts[:-1]), create=create)
    return parent, parts[-1]


def label(eje, path):
    return f"{eje}.{path}" if path else eje


def print_tree(node, prefix="", is_last=True, is_root=True):
    desc = node.get("desc") or "(sin desc)"
    if is_root:
        print(f"{node['name']}: {desc}")
        child_prefix = ""
    else:
        connector = "└─ " if is_last else "├─ "
        print(f"{prefix}{connector}{node['name']}: {desc}")
        child_prefix = prefix + ("   " if is_last else "│  ")
    childs = node.get("childs", [])
    for i, c in enumerate(childs):
        print_tree(c, child_prefix, is_last=(i == len(childs) - 1), is_root=False)


def cmd_tree(args, db):
    if not args.eje:
        for i, eje in enumerate(SECCIONES):
            print_tree(db[eje])
            if i < len(SECCIONES) - 1:
                print()
        return
    check_eje_valid(args.eje)
    node = resolve_path(db, args.eje, args.path, create=False)
    print_tree(node)


def cmd_list(args, db):
    if not args.eje:
        for eje in SECCIONES:
            n = db[eje]
            print(f"- {eje}: {n.get('desc') or ''} ({len(n['childs'])} hijo(s))")
        return
    check_eje_valid(args.eje)
    node = resolve_path(db, args.eje, args.path, create=False)
    childs = node.get("childs", [])
    if not childs:
        print(f"(sin hijos en {label(args.eje, args.path)}; nodo terminal)")
        return
    for c in childs:
        desc = c.get("desc") or "(sin descripción — regístrala en references/subejes.md)"
        n_hijos = len(c.get("childs", []))
        extra = f", {n_hijos} hijo(s)" if n_hijos else ""
        print(f"- {c['name']}: {desc}{extra}")


def cmd_show(args, db):
    check_eje_valid(args.eje)
    node = resolve_path(db, args.eje, args.path, create=False)
    if args.raw:
        print(json.dumps(node, ensure_ascii=False, indent=2))
        return
    print(f"Nodo: {label(args.eje, args.path)}")
    print(f"Desc: {node.get('desc') or '(sin descripción)'}")
    info = node.get("info")
    if not info:
        print("Info: (vacío)")
    else:
        print("Info:")
        print(info)
    childs = node.get("childs", [])
    if childs:
        nombres = ", ".join(c["name"] for c in childs)
        print(f"Hijos ({len(childs)}): {nombres}")
    else:
        print("Hijos: (ninguno — nodo terminal)")
    if "note" in node:
        print(f"Notas: {len(node['note'])} (ver con 'notas {args.eje}')")


def cmd_set(args, db):
    check_eje_valid(args.eje)
    parent, name = resolve_parent(db, args.eje, args.path, create=True)
    node = find_child(parent, name)
    is_new = node is None
    if is_new:
        node = new_node(name)
        parent["childs"].append(node)
    if args.desc is not None:
        node["desc"] = args.desc
    if args.info is not None:
        node["info"] = args.info
    save(db)
    accion = "creado" if is_new else "actualizado"
    print(f"OK: nodo {accion} {label(args.eje, args.path)}")
    if is_new and args.desc is None:
        print("Aviso: creado sin --desc; agrégala y regístralo en references/subejes.md")
    elif is_new:
        print("Recuerda registrarlo en references/subejes.md")
    print(json.dumps(node, ensure_ascii=False, indent=2))


def cmd_append(args, db):
    check_eje_valid(args.eje)
    parent, name = resolve_parent(db, args.eje, args.path, create=True)
    node = find_child(parent, name)
    is_new = node is None
    if is_new:
        node = new_node(name, desc=args.desc)
        parent["childs"].append(node)
    linea = f"[{now()}] {args.valor}"
    node["info"] = f"{node['info']}\n{linea}" if node.get("info") else linea
    save(db)
    print(f"OK: agregado a {label(args.eje, args.path)} -> {linea}")
    if is_new:
        print("Recuerda registrarlo en references/subejes.md")


def cmd_note(args, db):
    check_eje_valid(args.eje)
    note = db[args.eje].setdefault("note", [])
    next_id = max((n["id"] for n in note), default=0) + 1
    entry = {"id": next_id, "fecha": now(), "texto": args.valor}
    note.append(entry)
    save(db)
    print(f"OK: nota agregada -> {args.eje}#{next_id}: {args.valor!r}")
    print(f"Si esto se refleja en un nodo del árbol, cítala como '(ver nota {args.eje}#{next_id})' en su info.")


def cmd_notas_list(args, db):
    check_eje_valid(args.eje)
    note = db[args.eje].get("note", [])
    if not note:
        print(f"(sin notas en {args.eje})")
        return
    for n in note:
        print(f"[{args.eje}#{n['id']}] ({n['fecha']}) {n['texto']}")


def cmd_rm_nota(args, db):
    check_eje_valid(args.eje)
    note = db[args.eje].get("note", [])
    match = next((n for n in note if n["id"] == args.id), None)
    if match is None:
        sys.exit(f"Nota inexistente: {args.eje}#{args.id}")
    note.remove(match)
    save(db)
    print(f"OK: eliminada {args.eje}#{args.id}")


def cmd_rm(args, db):
    check_eje_valid(args.eje)
    parent, name = resolve_parent(db, args.eje, args.path, create=False)
    node = find_child(parent, name)
    if node is None:
        sys.exit(f"Nodo inexistente: {label(args.eje, args.path)}")
    if node["childs"] and not args.force:
        sys.exit(
            f"{label(args.eje, args.path)} tiene {len(node['childs'])} hijo(s) — "
            f"usa --force para borrar todo el subárbol"
        )
    parent["childs"] = [c for c in parent["childs"] if c["name"] != name]
    save(db)
    print(f"OK: eliminado {label(args.eje, args.path)} (quítalo también de references/subejes.md)")


def cmd_insights(args, db):
    lista = db["insights"]
    if not lista:
        print("(sin insights)")
        return
    for item in lista:
        print(f"[insight#{item['id']}] ({item['fecha']}) {item['texto']}")


def cmd_insight(args, db):
    lista = db["insights"]
    next_id = max((i["id"] for i in lista), default=0) + 1
    entry = {"id": next_id, "fecha": now(), "texto": args.valor}
    lista.append(entry)
    save(db)
    print(f"OK: insight agregado -> insight#{next_id}: {args.valor!r}")
    print("Si el usuario lo confirma: refléjalo en el nodo del árbol correspondiente y borra este insight con rm-insight (ya no es hipótesis, es dato confirmado).")


def cmd_rm_insight(args, db):
    lista = db["insights"]
    match = next((i for i in lista if i["id"] == args.id), None)
    if match is None:
        sys.exit(f"Insight inexistente: insight#{args.id}")
    lista.remove(match)
    save(db)
    print(f"OK: eliminado insight#{args.id} -> {match['texto']!r}")


def main():
    p = argparse.ArgumentParser(prog="profile.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("tree", help="estructura del árbol (nombres+desc), sin contenido")
    sp.add_argument("eje", nargs="?", choices=SECCIONES)
    sp.add_argument("path", nargs="?")
    sp.set_defaults(func=cmd_tree)

    sp = sub.add_parser("list", help="hijos directos de un nodo (nombres+desc), sin bajar más")
    sp.add_argument("eje", nargs="?", choices=SECCIONES)
    sp.add_argument("path", nargs="?")
    sp.set_defaults(func=cmd_list)

    sp = sub.add_parser("show", help="contenido (desc+info) de un nodo puntual + nombres de sus hijos")
    sp.add_argument("eje", choices=SECCIONES)
    sp.add_argument("path", nargs="?")
    sp.add_argument("--raw", action="store_true", help="dump JSON literal del nodo (debug)")
    sp.set_defaults(func=cmd_show)

    sp = sub.add_parser("set", help="crea o actualiza un nodo (desc y/o info, info siempre texto plano)")
    sp.add_argument("eje", choices=SECCIONES)
    sp.add_argument("path")
    sp.add_argument("--desc")
    sp.add_argument("--info", help="texto plano — reemplaza el info completo del nodo")
    sp.set_defaults(func=cmd_set)

    sp = sub.add_parser("append", help="agrega una línea fechada al info (texto) de un nodo; lo crea si falta")
    sp.add_argument("eje", choices=SECCIONES)
    sp.add_argument("path")
    sp.add_argument("valor")
    sp.add_argument("--desc", help="solo se usa si el nodo se crea recién ahora")
    sp.set_defaults(func=cmd_append)

    sp = sub.add_parser("note", help="agrega una nota cruda con id al eje (fuera del árbol)")
    sp.add_argument("eje", choices=SECCIONES)
    sp.add_argument("valor")
    sp.set_defaults(func=cmd_note)

    sp = sub.add_parser("notas", help="lista las notas de un eje con su id")
    sp.add_argument("eje", choices=SECCIONES)
    sp.set_defaults(func=cmd_notas_list)

    sp = sub.add_parser("rm-nota", help="elimina una nota por id")
    sp.add_argument("eje", choices=SECCIONES)
    sp.add_argument("id", type=int)
    sp.set_defaults(func=cmd_rm_nota)

    sp = sub.add_parser("rm", help="elimina un nodo completo")
    sp.add_argument("eje", choices=SECCIONES)
    sp.add_argument("path")
    sp.add_argument("--force", action="store_true", help="borra aunque tenga hijos")
    sp.set_defaults(func=cmd_rm)

    sp = sub.add_parser("insights", help="listar conclusiones propias (no reportadas por el usuario)")
    sp.set_defaults(func=cmd_insights)

    sp = sub.add_parser("insight", help="agregar una conclusión propia")
    sp.add_argument("valor")
    sp.set_defaults(func=cmd_insight)

    sp = sub.add_parser("rm-insight", help="elimina un insight por id")
    sp.add_argument("id", type=int)
    sp.set_defaults(func=cmd_rm_insight)

    args = p.parse_args()
    db = load()
    args.func(args, db)


if __name__ == "__main__":
    main()
