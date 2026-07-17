"""Crea la estructura del workspace de Notion para second-brain (correr UNA sola vez).

Requiere las variables de entorno NOTION_TOKEN y NOTION_ROOT_PAGE_ID (ver Task 1
del plan: crear la integración interna en notion.so/my-integrations, compartir
una página raíz con ella, y tomar el token + el ID de esa página de su URL).

Uso:
    NOTION_TOKEN=secret_xxx NOTION_ROOT_PAGE_ID=xxxx python3 setup_workspace.py

Escribe el resultado en ../../references/notion-ids.json.
"""
import json
import os

from notion_client import Client

EJES = {
    "salud": "Salud", "emocional": "Emocional", "proyectos": "Proyectos",
    "trabajo": "Trabajo", "academico": "Académico", "general": "General",
}
TODO_TAGS = ["tesis", "trabajo", "personal"]
TODO_STATES = ["pendiente", "en_progreso", "bloqueada", "hecha", "cancelada"]


def main():
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    root_id = os.environ["NOTION_ROOT_PAGE_ID"]

    perfil = notion.pages.create(
        parent={"page_id": root_id},
        properties={"title": [{"text": {"content": "Perfil"}}]},
    )

    eje_page_ids = {}
    for key, titulo in EJES.items():
        page = notion.pages.create(
            parent={"page_id": perfil["id"]},
            properties={"title": [{"text": {"content": titulo}}]},
        )
        eje_page_ids[key] = page["id"]

    # Notion (API 2025-09+): una "database" es solo un contenedor; el schema real
    # (las propiedades) vive en su "data source" — hay que pasarlo anidado en
    # `initial_data_source` al crear, y usar el `data_source_id` (no el
    # `database_id`) para crear/consultar filas.
    notas_db = notion.databases.create(
        parent={"type": "page_id", "page_id": root_id},
        title=[{"text": {"content": "Notas"}}],
        initial_data_source={
            "properties": {
                "Texto": {"title": {}},
                "Eje": {"select": {"options": [{"name": v} for v in EJES.values()]}},
                "Fecha": {"date": {}},
                "ID": {"unique_id": {"prefix": "NOTE"}},
            }
        },
    )

    insights_db = notion.databases.create(
        parent={"type": "page_id", "page_id": root_id},
        title=[{"text": {"content": "Insights"}}],
        initial_data_source={
            "properties": {
                "Texto": {"title": {}},
                "Fecha": {"date": {}},
                "ID": {"unique_id": {"prefix": "INS"}},
            }
        },
    )

    todos_db = notion.databases.create(
        parent={"type": "page_id", "page_id": root_id},
        title=[{"text": {"content": "Todos"}}],
        initial_data_source={
            "properties": {
                "Name": {"title": {}},
                "Fecha": {"date": {}},
                "Tags": {"multi_select": {"options": [{"name": t} for t in TODO_TAGS]}},
                "Estado": {"select": {"options": [{"name": s} for s in TODO_STATES]}},
                "ID": {"unique_id": {"prefix": "TODO"}},
            }
        },
    )

    research = notion.pages.create(
        parent={"page_id": root_id},
        properties={"title": [{"text": {"content": "Research"}}]},
    )

    ids = {
        "root_page_id": root_id,
        "perfil_page_id": perfil["id"],
        "eje_page_ids": eje_page_ids,
        "notas_db_id": notas_db["id"],
        "notas_ds_id": notas_db["data_sources"][0]["id"],
        "insights_db_id": insights_db["id"],
        "insights_ds_id": insights_db["data_sources"][0]["id"],
        "todos_db_id": todos_db["id"],
        "todos_ds_id": todos_db["data_sources"][0]["id"],
        "research_page_id": research["id"],
    }
    out_path = os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")
    with open(out_path, "w") as f:
        json.dump(ids, f, indent=2, ensure_ascii=False)
    print(f"IDs escritos en {out_path}")


if __name__ == "__main__":
    main()
