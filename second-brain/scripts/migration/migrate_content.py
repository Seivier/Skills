"""Migra el contenido de second-brain (perfil, notas, insights, todos, research)
al workspace de Notion creado por setup_workspace.py. Correr UNA sola vez, con
NOTION_TOKEN en el entorno y references/notion-ids.json ya generado.

Uso:
    NOTION_TOKEN=secret_xxx python3 migrate_content.py
"""
import glob
import json
import os

from notion_client import Client

from convert import (
    flatten_profile_tree,
    note_to_db_properties,
    todo_to_db_properties,
    markdown_to_blocks,
)

EJES = ["salud", "emocional", "proyectos", "trabajo", "academico", "general"]
EJE_TITULOS = {
    "salud": "Salud", "emocional": "Emocional", "proyectos": "Proyectos",
    "trabajo": "Trabajo", "academico": "Académico", "general": "General",
}


def _page_content_children(desc, info):
    children = [{
        "type": "callout",
        "callout": {"rich_text": [{"text": {"content": f"Resumen: {desc}"}}], "icon": {"emoji": "📝"}},
    }]
    if info:
        for line in info.split("\n"):
            if line.strip():
                children.append({"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": line}}]}})
    return children


def migrate_profile_tree(notion, profile_json_path, ids):
    with open(profile_json_path) as f:
        profile = json.load(f)

    for eje in EJES:
        eje_node = profile[eje]
        flat = flatten_profile_tree(eje_node)
        created_ids = [None] * len(flat)
        # el nodo raíz del eje (índice 0) ya existe (creado en setup_workspace.py)
        created_ids[0] = ids["eje_page_ids"][eje]
        notion.blocks.children.append(
            block_id=created_ids[0],
            children=_page_content_children(flat[0]["desc"], flat[0]["info"]),
        )
        for i, item in enumerate(flat[1:], start=1):
            parent_id = created_ids[item["parent_index"]]
            page = notion.pages.create(
                parent={"page_id": parent_id},
                properties={"title": [{"text": {"content": item["name"]}}]},
                children=_page_content_children(item["desc"], item["info"]),
            )
            created_ids[i] = page["id"]


def migrate_notes_and_insights(notion, profile_json_path, ids):
    with open(profile_json_path) as f:
        profile = json.load(f)

    for eje in EJES:
        for note in profile[eje].get("note", []):
            notion.pages.create(
                parent={"type": "data_source_id", "data_source_id": ids["notas_ds_id"]},
                properties=note_to_db_properties(note, eje=EJE_TITULOS[eje]),
            )

    for insight in profile.get("insights", []):
        notion.pages.create(
            parent={"type": "data_source_id", "data_source_id": ids["insights_ds_id"]},
            properties=note_to_db_properties(insight),
        )


def migrate_todos(notion, todos_json_path, archive_json_path, ids):
    for path in (todos_json_path, archive_json_path):
        if not os.path.exists(path):
            continue
        with open(path) as f:
            data = json.load(f)
        for todo in data["todos"]:
            notion.pages.create(
                parent={"type": "data_source_id", "data_source_id": ids["todos_ds_id"]},
                properties=todo_to_db_properties(todo),
            )


def migrate_research(notion, research_dir, ids):
    for md_path in sorted(glob.glob(os.path.join(research_dir, "*.md"))):
        if os.path.basename(md_path) == "index.md":
            continue
        with open(md_path) as f:
            text = f.read()
        title = os.path.splitext(os.path.basename(md_path))[0]
        notion.pages.create(
            parent={"page_id": ids["research_page_id"]},
            properties={"title": [{"text": {"content": title}}]},
            children=markdown_to_blocks(text),
        )


if __name__ == "__main__":
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    ids_path = os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")
    with open(ids_path) as f:
        ids = json.load(f)

    profile_path = os.path.expanduser("~/.claude/second-brain/profile.json")
    migrate_profile_tree(notion, profile_path, ids)
    print("Árbol de perfil migrado.")

    migrate_notes_and_insights(notion, profile_path, ids)
    print("Notas e insights migrados.")

    migrate_todos(
        notion,
        os.path.expanduser("~/.claude/second-brain/todos.json"),
        os.path.expanduser("~/.claude/second-brain/todos-archive.json"),
        ids,
    )
    print("Todos migrados.")

    migrate_research(notion, os.path.expanduser("~/.claude/second-brain/research"), ids)
    print("Investigaciones migradas.")
