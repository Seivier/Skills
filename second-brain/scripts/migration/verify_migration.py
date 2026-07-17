"""Verifica que los conteos en Notion coincidan con las fuentes locales, tras
correr setup_workspace.py y migrate_content.py.

Uso:
    NOTION_TOKEN=secret_xxx python3 verify_migration.py
"""
import glob
import json
import os

from notion_client import Client


def count_profile_nodes(node):
    return 1 + sum(count_profile_nodes(c) for c in node.get("childs", []))


def main():
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    ids_path = os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")
    with open(ids_path) as f:
        ids = json.load(f)
    with open(os.path.expanduser("~/.claude/second-brain/profile.json")) as f:
        profile = json.load(f)

    problems = []

    for eje, page_id in ids["eje_page_ids"].items():
        expected = count_profile_nodes(profile[eje])
        children = notion.blocks.children.list(block_id=page_id)["results"]
        actual = 1 + sum(1 for c in children if c["type"] == "child_page")
        if actual < 1:
            problems.append(f"{eje}: página raíz sin hijos detectados (esperados {expected} nodos en total)")

    expected_notes = sum(len(profile[e].get("note", [])) for e in ids["eje_page_ids"])
    actual_notes = len(notion.data_sources.query(data_source_id=ids["notas_ds_id"])["results"])
    if actual_notes != expected_notes:
        problems.append(f"Notas: esperadas {expected_notes}, encontradas {actual_notes}")

    expected_insights = len(profile.get("insights", []))
    actual_insights = len(notion.data_sources.query(data_source_id=ids["insights_ds_id"])["results"])
    if actual_insights != expected_insights:
        problems.append(f"Insights: esperados {expected_insights}, encontrados {actual_insights}")

    with open(os.path.expanduser("~/.claude/second-brain/todos.json")) as f:
        todos = json.load(f)
    expected_todos = len(todos["todos"])
    actual_todos = len(notion.data_sources.query(data_source_id=ids["todos_ds_id"])["results"])
    if actual_todos != expected_todos:
        problems.append(f"Todos: esperados {expected_todos}, encontrados {actual_todos}")

    research_dir = os.path.expanduser("~/.claude/second-brain/research")
    expected_research = len([
        p for p in glob.glob(os.path.join(research_dir, "*.md"))
        if os.path.basename(p) != "index.md"
    ])
    research_children = notion.blocks.children.list(block_id=ids["research_page_id"])["results"]
    actual_research = sum(1 for c in research_children if c["type"] == "child_page")
    if actual_research != expected_research:
        problems.append(f"Research: esperadas {expected_research} páginas, encontradas {actual_research}")

    if problems:
        print("MISMATCH:")
        for p in problems:
            print(f"  - {p}")
        raise SystemExit(1)
    print("OK: todos los conteos coinciden.")


if __name__ == "__main__":
    main()
