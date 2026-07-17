#!/usr/bin/env python3
# DEPRECADO (2026-07-13): reemplazado por el MCP de Notion, ver
# references/notion-portability-design.md y references/notion-portability-plan.md.
# Se conserva sin borrar como referencia histórica; SKILL.md ya no lo invoca.
"""Gestor del TODO del usuario — única vía autorizada para tocar los datos.

Los todos viven en ~/.claude/second-brain/todos.json. Tags y estados son
vocabularios cerrados (ver TAGS y STATES). Todo cambio de fecha o estado queda
registrado en el historial de cada tarea, lo que permite analizar atrasos con
`delays`.

Uso:
    todo.py add "descripción" --date 2026-07-15 --tags tesis [trabajo ...]
    todo.py list [--state S] [--tag T] [--today] [--overdue] [--all]
    todo.py set ID [--desc "..."] [--date YYYY-MM-DD] [--tags T ...] [--state S]
    todo.py done ID              # atajo de set --state hecha
    todo.py rm ID --force        # borrar de verdad (solo si el usuario lo pide explícito)
    todo.py delays               # análisis de reprogramaciones y cierres tardíos
    todo.py archive [--before YYYY-MM-DD]   # mueve hechas/canceladas viejas al archivo
    todo.py announce [--quiet]   # regenera el anuncio de arranque en settings.json
"""

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

TODO_DIR = Path.home() / ".claude" / "second-brain"
DATA = TODO_DIR / "todos.json"
ARCHIVE = TODO_DIR / "todos-archive.json"
SETTINGS = Path.home() / ".claude" / "settings.json"

TAGS = ["tesis", "trabajo", "personal"]
STATES = ["pendiente", "en_progreso", "bloqueada", "hecha", "cancelada"]
ACTIVE = ["pendiente", "en_progreso", "bloqueada"]


def now():
    return datetime.now().isoformat(timespec="seconds")


def load(path=DATA):
    if not path.exists():
        return {"version": 1, "next_id": 1, "todos": []}
    return json.loads(path.read_text())


def save(db, path=DATA):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(db, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def parse_date(s):
    try:
        return date.fromisoformat(s).isoformat()
    except ValueError:
        sys.exit(f"Fecha inválida: {s!r} (formato YYYY-MM-DD)")


def find(db, id_):
    for t in db["todos"]:
        if t["id"] == id_:
            return t
    sys.exit(f"No existe un todo con id {id_}.")


def fmt(t):
    today = date.today().isoformat()
    late = " ⚠️atrasada" if t["state"] in ACTIVE and t["date"] < today else ""
    tags = ",".join(t["tags"])
    return f"#{t['id']:<3} [{t['state']:<11}] {t['date']}{late}  ({tags})  {t['description']}"


# ---------------------------------------------------------------- comandos

def cmd_add(args):
    db = load()
    t = {
        "id": db["next_id"],
        "description": args.description,
        "date": parse_date(args.date),
        "tags": sorted(set(args.tags)),
        "state": args.state,
        "created_at": now(),
        "updated_at": now(),
        "history": [],
    }
    db["next_id"] += 1
    db["todos"].append(t)
    save(db)
    print(f"Añadido: {fmt(t)}")
    refresh_announcement()


def cmd_list(args):
    db = load()
    todos = db["todos"]
    today = date.today().isoformat()
    if not args.all and not args.state:
        todos = [t for t in todos if t["state"] in ACTIVE]
    if args.state:
        todos = [t for t in todos if t["state"] == args.state]
    if args.tag:
        todos = [t for t in todos if args.tag in t["tags"]]
    if args.today:
        todos = [t for t in todos if t["date"] == today]
    if args.overdue:
        todos = [t for t in todos if t["state"] in ACTIVE and t["date"] < today]
    if not todos:
        print("Sin resultados.")
        return
    for t in sorted(todos, key=lambda t: (t["date"], t["id"])):
        print(fmt(t))


def cmd_set(args):
    db = load()
    t = find(db, args.id)
    changes = []
    if args.desc is not None and args.desc != t["description"]:
        changes.append(("description", t["description"], args.desc))
        t["description"] = args.desc
    if args.date is not None:
        new = parse_date(args.date)
        if new != t["date"]:
            changes.append(("date", t["date"], new))
            t["date"] = new
    if args.tags is not None:
        new = sorted(set(args.tags))
        if new != t["tags"]:
            changes.append(("tags", t["tags"], new))
            t["tags"] = new
    if args.state is not None and args.state != t["state"]:
        changes.append(("state", t["state"], args.state))
        t["state"] = args.state
    if not changes:
        print("Nada que cambiar.")
        return
    stamp = now()
    t["updated_at"] = stamp
    for field, old, new in changes:
        t["history"].append({"at": stamp, "field": field, "from": old, "to": new})
    save(db)
    print(f"Actualizado: {fmt(t)}")
    refresh_announcement()


def cmd_done(args):
    args.desc = args.date = args.tags = None
    args.state = "hecha"
    cmd_set(args)


def cmd_rm(args):
    if not args.force:
        sys.exit("rm borra sin dejar rastro; el flujo normal es `set ID --state cancelada`. "
                 "Si de verdad quieres borrar, repite con --force.")
    db = load()
    t = find(db, args.id)
    db["todos"].remove(t)
    save(db)
    print(f"Eliminado: #{t['id']} {t['description']}")
    refresh_announcement()


def cmd_delays(args):
    db = load()
    today = date.today()
    total_moves, total_days = 0, 0
    print("== Reprogramaciones ==")
    for t in db["todos"]:
        moves = [h for h in t["history"] if h["field"] == "date"]
        if not moves:
            continue
        days = sum((date.fromisoformat(h["to"]) - date.fromisoformat(h["from"])).days
                   for h in moves)
        total_moves += len(moves)
        total_days += days
        detail = "; ".join(f"{h['from']} → {h['to']} ({h['at'][:10]})" for h in moves)
        print(f"#{t['id']} {t['description']}: {len(moves)} cambio(s), {days:+d} días. {detail}")
    if total_moves == 0:
        print("Ninguna tarea reprogramada.")
    else:
        print(f"Total: {total_moves} reprogramaciones, {total_days:+d} días acumulados.")

    print("\n== Cierres tardíos ==")
    late_any = False
    for t in db["todos"]:
        if t["state"] != "hecha":
            continue
        done_at = next((h["at"][:10] for h in reversed(t["history"])
                        if h["field"] == "state" and h["to"] == "hecha"), None)
        if done_at and done_at > t["date"]:
            delta = (date.fromisoformat(done_at) - date.fromisoformat(t["date"])).days
            late_any = True
            print(f"#{t['id']} {t['description']}: límite {t['date']}, hecha {done_at} (+{delta} días)")
    if not late_any:
        print("Ninguna tarea cerrada después de su fecha límite.")

    overdue = [t for t in db["todos"] if t["state"] in ACTIVE and t["date"] < today.isoformat()]
    if overdue:
        print("\n== Atrasadas ahora mismo ==")
        for t in sorted(overdue, key=lambda t: t["date"]):
            delta = (today - date.fromisoformat(t["date"])).days
            print(f"#{t['id']} {t['description']}: vencida hace {delta} día(s) ({t['date']})")


def cmd_archive(args):
    db = load()
    cutoff = parse_date(args.before) if args.before else date.today().isoformat()
    keep, move = [], []
    for t in db["todos"]:
        if t["state"] in ("hecha", "cancelada") and t["updated_at"][:10] < cutoff:
            move.append(t)
        else:
            keep.append(t)
    if not move:
        print("Nada que archivar.")
        return
    arch = load(ARCHIVE)
    arch.setdefault("next_id", 0)  # el archivo no asigna ids
    arch["todos"].extend(move)
    db["todos"] = keep
    save(arch, ARCHIVE)
    save(db)
    print(f"Archivadas {len(move)} tareas en {ARCHIVE.name}.")


def build_announcement(db):
    today = date.today().isoformat()
    items = [t for t in db["todos"] if t["state"] in ACTIVE and t["date"] <= today]
    if not items:
        return None
    parts = []
    for t in sorted(items, key=lambda t: (t["date"], t["id"])):
        mark = "⚠️" if t["date"] < today else ""
        mark += "🔒" if t["state"] == "bloqueada" else ""
        parts.append(f"{mark}{t['description']} [{','.join(t['tags'])}]")
    return f"📋 TODO {date.today():%d/%m}: " + " • ".join(parts)


def refresh_announcement():
    try:
        cmd_announce(argparse.Namespace(quiet=True))
    except Exception as e:  # el anuncio nunca debe romper una operación de datos
        print(f"(aviso: no se pudo actualizar el anuncio: {e})", file=sys.stderr)


def cmd_announce(args):
    db = load()
    settings = json.loads(SETTINGS.read_text())
    text = build_announcement(db)
    settings["companyAnnouncements"] = [text] if text else []
    tmp = SETTINGS.with_name(SETTINGS.name + ".tmp")
    tmp.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(SETTINGS)
    if not args.quiet:
        print(text or "Sin tareas para hoy; anuncio vacío.")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("add", help="añadir una tarea")
    sp.add_argument("description")
    sp.add_argument("--date", required=True, help="fecha límite YYYY-MM-DD")
    sp.add_argument("--tags", nargs="+", choices=TAGS, required=True)
    sp.add_argument("--state", choices=STATES, default="pendiente")
    sp.set_defaults(func=cmd_add)

    sp = sub.add_parser("list", help="listar tareas (por defecto solo activas)")
    sp.add_argument("--state", choices=STATES)
    sp.add_argument("--tag", choices=TAGS)
    sp.add_argument("--today", action="store_true")
    sp.add_argument("--overdue", action="store_true")
    sp.add_argument("--all", action="store_true")
    sp.set_defaults(func=cmd_list)

    sp = sub.add_parser("set", help="modificar una tarea (queda en su historial)")
    sp.add_argument("id", type=int)
    sp.add_argument("--desc")
    sp.add_argument("--date", help="nueva fecha límite YYYY-MM-DD")
    sp.add_argument("--tags", nargs="+", choices=TAGS)
    sp.add_argument("--state", choices=STATES)
    sp.set_defaults(func=cmd_set)

    sp = sub.add_parser("done", help="marcar como hecha")
    sp.add_argument("id", type=int)
    sp.set_defaults(func=cmd_done)

    sp = sub.add_parser("rm", help="borrar definitivamente (requiere --force)")
    sp.add_argument("id", type=int)
    sp.add_argument("--force", action="store_true")
    sp.set_defaults(func=cmd_rm)

    sp = sub.add_parser("delays", help="análisis de atrasos y reprogramaciones")
    sp.set_defaults(func=cmd_delays)

    sp = sub.add_parser("archive", help="mover hechas/canceladas viejas al archivo")
    sp.add_argument("--before", help="solo las actualizadas antes de esta fecha")
    sp.set_defaults(func=cmd_archive)

    sp = sub.add_parser("announce", help="regenerar el anuncio de arranque")
    sp.add_argument("--quiet", action="store_true")
    sp.set_defaults(func=cmd_announce)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
