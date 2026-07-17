"""Funciones puras de conversión de datos locales (profile.json/todos.json/research)
a las estructuras que espera la API de Notion. Sin llamadas de red — todo lo que
recibe y devuelve son dicts/listas planas, para poder testearlo sin un workspace real.
"""

TODO_TAGS = {"tesis", "trabajo", "personal"}
TODO_STATES = {"pendiente", "en_progreso", "bloqueada", "hecha", "cancelada"}


def flatten_profile_tree(node, parent_index=None, _out=None):
    out = _out if _out is not None else []
    my_index = len(out)
    out.append({
        "name": node["name"],
        "desc": node.get("desc") or "",
        "info": node.get("info"),
        "parent_index": parent_index,
    })
    for child in node.get("childs", []):
        flatten_profile_tree(child, my_index, out)
    return out


def note_to_db_properties(note, eje=None):
    props = {
        "Texto": {"title": _rich_text(note["texto"])},
        "Fecha": {"date": {"start": note["fecha"]}},
    }
    if eje is not None:
        props["Eje"] = {"select": {"name": eje}}
    return props


def todo_to_db_properties(todo):
    for tag in todo["tags"]:
        if tag not in TODO_TAGS:
            raise ValueError(f"tag desconocido: {tag}")
    if todo["state"] not in TODO_STATES:
        raise ValueError(f"estado desconocido: {todo['state']}")
    return {
        "Name": {"title": _rich_text(todo["description"])},
        "Fecha": {"date": {"start": todo["date"]}} if todo.get("date") else {"date": None},
        "Tags": {"multi_select": [{"name": t} for t in todo["tags"]]},
        "Estado": {"select": {"name": todo["state"]}},
    }


NOTION_RICH_TEXT_LIMIT = 2000


def _rich_text(content):
    """Notion rechaza cualquier rich_text.text.content de más de 2000
    caracteres — partirlo en varios segmentos (se concatenan visualmente)."""
    if not content:
        return [{"text": {"content": ""}}]
    chunks = [
        content[i:i + NOTION_RICH_TEXT_LIMIT]
        for i in range(0, len(content), NOTION_RICH_TEXT_LIMIT)
    ]
    return [{"text": {"content": c}} for c in chunks]


def markdown_to_blocks(markdown_text):
    blocks = []
    for raw_para in markdown_text.strip().split("\n\n"):
        para = raw_para.strip("\n")
        if not para:
            continue
        lines = para.splitlines()
        first_line = lines[0]
        if first_line.startswith("## "):
            blocks.append({"type": "heading_2", "heading_2": {
                "rich_text": _rich_text(first_line[3:])}})
            continue
        if first_line.startswith("# "):
            blocks.append({"type": "heading_1", "heading_1": {
                "rich_text": _rich_text(first_line[2:])}})
            continue
        if all(l.startswith("- ") for l in lines):
            for l in lines:
                blocks.append({"type": "bulleted_list_item", "bulleted_list_item": {
                    "rich_text": _rich_text(l[2:])}})
            continue
        blocks.append({"type": "paragraph", "paragraph": {
            "rich_text": _rich_text(para)}})
    return blocks
