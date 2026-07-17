import pytest

from convert import (
    flatten_profile_tree,
    note_to_db_properties,
    todo_to_db_properties,
    markdown_to_blocks,
)


def test_flatten_single_node_no_children():
    node = {"name": "ejercicio", "desc": "d", "info": "i", "childs": []}
    assert flatten_profile_tree(node) == [
        {"name": "ejercicio", "desc": "d", "info": "i", "parent_index": None}
    ]


def test_flatten_nested_tree_tracks_parent_index():
    node = {
        "name": "salud", "desc": "eje", "info": None,
        "childs": [
            {"name": "ejercicio", "desc": "d1", "info": "i1", "childs": []},
            {"name": "dieta", "desc": "d2", "info": None, "childs": [
                {"name": "restricciones", "desc": "d3", "info": "i3", "childs": []},
            ]},
        ],
    }
    result = flatten_profile_tree(node)
    assert [r["name"] for r in result] == ["salud", "ejercicio", "dieta", "restricciones"]
    assert result[0]["parent_index"] is None
    assert result[1]["parent_index"] == 0
    assert result[2]["parent_index"] == 0
    assert result[3]["parent_index"] == 2


def test_flatten_missing_desc_defaults_to_empty_string():
    node = {"name": "x", "info": None, "childs": []}
    assert flatten_profile_tree(node)[0]["desc"] == ""


def test_note_to_db_properties_with_eje():
    note = {"id": 1, "fecha": "2026-07-12T22:03:47", "texto": "Peso actual ~80kg"}
    props = note_to_db_properties(note, eje="Salud")
    assert props["Texto"]["title"][0]["text"]["content"] == "Peso actual ~80kg"
    assert props["Fecha"]["date"]["start"] == "2026-07-12T22:03:47"
    assert props["Eje"]["select"]["name"] == "Salud"


def test_note_to_db_properties_without_eje_omits_eje_key():
    note = {"id": 1, "fecha": "2026-07-12T22:03:47", "texto": "insight libre"}
    props = note_to_db_properties(note)
    assert "Eje" not in props


def test_todo_to_db_properties_valid():
    todo = {
        "description": "Escribir introducción de la tesis", "date": "2026-07-10",
        "tags": ["tesis"], "state": "hecha",
    }
    props = todo_to_db_properties(todo)
    assert props["Name"]["title"][0]["text"]["content"] == todo["description"]
    assert props["Fecha"]["date"]["start"] == "2026-07-10"
    assert props["Tags"]["multi_select"] == [{"name": "tesis"}]
    assert props["Estado"]["select"]["name"] == "hecha"


def test_todo_to_db_properties_no_date_sets_null_date():
    todo = {"description": "x", "date": None, "tags": [], "state": "pendiente"}
    assert todo_to_db_properties(todo)["Fecha"]["date"] is None


def test_todo_to_db_properties_rejects_unknown_tag():
    todo = {"description": "x", "date": "2026-07-10", "tags": ["no-existe"], "state": "pendiente"}
    with pytest.raises(ValueError):
        todo_to_db_properties(todo)


def test_todo_to_db_properties_rejects_unknown_state():
    todo = {"description": "x", "date": "2026-07-10", "tags": [], "state": "no-existe"}
    with pytest.raises(ValueError):
        todo_to_db_properties(todo)


def test_markdown_to_blocks_heading_and_paragraph():
    md = "# Título\n\nUn párrafo simple."
    blocks = markdown_to_blocks(md)
    assert blocks[0]["type"] == "heading_1"
    assert blocks[0]["heading_1"]["rich_text"][0]["text"]["content"] == "Título"
    assert blocks[1]["type"] == "paragraph"
    assert blocks[1]["paragraph"]["rich_text"][0]["text"]["content"] == "Un párrafo simple."


def test_markdown_to_blocks_subheading():
    blocks = markdown_to_blocks("## Subtítulo\n\ntexto")
    assert blocks[0]["type"] == "heading_2"
    assert blocks[0]["heading_2"]["rich_text"][0]["text"]["content"] == "Subtítulo"


def test_markdown_to_blocks_bullet_list():
    md = "- primero\n- segundo\n- tercero"
    blocks = markdown_to_blocks(md)
    assert len(blocks) == 3
    assert all(b["type"] == "bulleted_list_item" for b in blocks)
    assert blocks[1]["bulleted_list_item"]["rich_text"][0]["text"]["content"] == "segundo"


def test_markdown_to_blocks_skips_blank_paragraphs():
    blocks = markdown_to_blocks("texto uno\n\n\n\ntexto dos")
    assert len(blocks) == 2


def test_markdown_to_blocks_splits_long_paragraph_into_rich_text_chunks():
    long_para = "x" * 3127
    blocks = markdown_to_blocks(long_para)
    assert len(blocks) == 1
    segments = blocks[0]["paragraph"]["rich_text"]
    assert all(len(s["text"]["content"]) <= 2000 for s in segments)
    assert "".join(s["text"]["content"] for s in segments) == long_para
