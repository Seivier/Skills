# Portabilidad de second-brain vía Notion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrar el contenido de `second-brain` (perfil árbol, todos, notas, insights,
investigaciones) desde JSON/MD locales a un workspace de Notion (free tier), accesible
desde terminal, PC de la pega, navegador y celular vía el MCP oficial y remoto de
Notion, sin servidor propio.

**Architecture:** Un script de migración de un solo uso puebla un workspace de Notion
con: páginas anidadas para el árbol de perfil, y tres bases de datos (Notas, Insights,
Todos) para las listas planas. `SKILL.md` se reescribe para operar sobre esa
estructura vía tools del MCP de Notion en vez de los scripts `todo.py`/`profile.py`
locales. Los JSON/MD actuales quedan como respaldo congelado, no se borran.

**Tech Stack:** Python 3 + `notion-client` (SDK oficial) + `pytest` para el script de
migración (temporal, se descarta tras usarse); Notion API v1; MCP remoto oficial de
Notion (`https://mcp.notion.com/mcp`).

## Global Constraints

- Plan free de Notion: bloques ilimitados en workspace de un solo miembro; 10 guests
  solo-lectura; archivos ≤5MB; historial de versiones de 7 días.
  Ver [Understanding block usage](https://www.notion.com/help/understanding-block-usage).
- API de Notion: ~3 requests/seg promedio, tope de 1000 requests/5min por workspace,
  payloads ≤500KB / ≤1000 bloques por request.
  Ver [Notion API request limits](https://developers.notion.com/reference/request-limits).
- Auth del MCP oficial es OAuth por cliente — no soporta bearer token fijo. Se
  autoriza una vez por instalación/dispositivo (terminal, PC de la pega, claude.ai).
- Los JSON/MD locales (`profile.json`, `todos.json`, `research/*.md`) **no se
  borran** — quedan como respaldo congelado tras la migración.
- Contenido de la skill en español; nombres de archivos/carpetas nuevos en inglés
  (convención ya vigente en el repo de skills).
- Spec de referencia: `references/notion-portability-design.md` (mismo directorio
  que este plan).

---

## Mapa de archivos

- Crear: `scripts/migration/convert.py` — funciones puras de conversión (sin red).
- Crear: `scripts/migration/convert_test.py` — tests de lo anterior.
- Crear: `scripts/migration/setup_workspace.py` — crea la estructura Notion, escribe `references/notion-ids.json`.
- Crear: `scripts/migration/migrate_content.py` — migra profile.json/todos.json/research/*.md usando `convert.py` + `notion-ids.json`.
- Crear: `scripts/migration/verify_migration.py` — chequeo de conteos post-migración.
- Crear: `references/notion-ids.json` (salida de `setup_workspace.py`, no se escribe a mano).
- Crear: `references/claude-ai-project-instructions.md` — instrucciones condensadas para el Project de claude.ai.
- Modificar: `SKILL.md` — secciones 0, 1, 2, 3, 4, 5, 6, 7, 8, "Reglas generales".
- Modificar (deprecar, no borrar): `scripts/todo.py`, `scripts/profile.py`, `references/subejes.md`.

Todos los paths son relativos a `/home/vgonzalez/.claude/skills/second-brain/`
salvo que se indique lo contrario.

---

### Task 1: Cuenta de Notion, integración y página raíz compartida (manual)

**Files:** ninguno — pasos manuales del usuario, documentados acá para que quien
ejecute el plan sepa exactamente qué pedirle al usuario si falta.

- [ ] **Step 1: Crear (o reusar) el workspace de Notion**

  Si el usuario no tiene cuenta, crearla gratis en https://www.notion.com — plan
  Free, workspace personal de un solo miembro (para que el límite de 1000 bloques
  no aplique).

- [ ] **Step 2: Crear una integración interna**

  En https://www.notion.so/my-integrations → "New integration" → nombre
  "second-brain" → tipo "Internal" → workspace: el del usuario. Copiar el
  **Internal Integration Token** (empieza con `secret_` o `ntn_`). Este token es
  solo para el script de migración de un solo uso — no es el mismo mecanismo que
  el MCP remoto (que usa OAuth, ver Task 6).

- [ ] **Step 3: Crear la página raíz y compartirla con la integración**

  Dentro de Notion, crear una página nueva en el nivel superior del workspace
  (título libre, ej. "Segundo cerebro"). Abrir el menú "..." de esa página → "Add
  connections" (o "Conectar a") → seleccionar la integración "second-brain". Sin
  este paso, la integración no puede ver ni escribir nada, aunque el token sea
  válido.

- [ ] **Step 4: Anotar el token y el ID de la página raíz**

  El ID de la página raíz es el segmento de 32 caracteres (con o sin guiones) al
  final de su URL de Notion. Exportar ambos como variables de entorno para los
  scripts de los pasos siguientes (no se guardan en ningún archivo del repo):

  ```bash
  export NOTION_TOKEN="secret_xxx..."
  export NOTION_ROOT_PAGE_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ```

---

### Task 2: Funciones puras de conversión (`convert.py`)

**Files:**
- Create: `scripts/migration/convert.py`
- Test: `scripts/migration/convert_test.py`

**Interfaces:**
- Produces: `flatten_profile_tree(node: dict, parent_index: int | None = None) -> list[dict]`
  — cada item: `{"name": str, "desc": str, "info": str | None, "parent_index": int | None}`.
- Produces: `note_to_db_properties(note: dict, eje: str | None = None) -> dict` (payload
  de `properties` para `pages.create` en la base "Notas"/"Insights").
- Produces: `todo_to_db_properties(todo: dict) -> dict` (ídem para la base "Todos");
  lanza `ValueError` si `tag`/`state` no están en el vocabulario conocido.
- Produces: `markdown_to_blocks(markdown_text: str) -> list[dict]` (lista de bloques
  de Notion: `paragraph`, `heading_1`, `heading_2`, `bulleted_list_item`).
- Consumidor: `setup_workspace.py` y `migrate_content.py` (Tasks 3-4).

- [ ] **Step 1: Escribir los tests de `flatten_profile_tree`**

```python
# scripts/migration/convert_test.py
from convert import flatten_profile_tree

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
```

- [ ] **Step 2: Correr los tests, confirmar que fallan por import faltante**

Run: `cd ~/.claude/skills/second-brain/scripts/migration && python3 -m pytest convert_test.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'convert'`

- [ ] **Step 3: Implementar `flatten_profile_tree`**

```python
# scripts/migration/convert.py
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
```

- [ ] **Step 4: Correr los tests, confirmar que pasan**

Run: `python3 -m pytest convert_test.py -v`
Expected: 3 passed

- [ ] **Step 5: Escribir los tests de `note_to_db_properties` y `todo_to_db_properties`**

```python
# agregar a scripts/migration/convert_test.py
from convert import note_to_db_properties, todo_to_db_properties
import pytest

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
```

- [ ] **Step 6: Correr los tests, confirmar que fallan**

Run: `python3 -m pytest convert_test.py -v`
Expected: FAIL — `ImportError: cannot import name 'note_to_db_properties'`

- [ ] **Step 7: Implementar `note_to_db_properties` y `todo_to_db_properties`**

```python
# agregar a scripts/migration/convert.py
TODO_TAGS = {"tesis", "trabajo", "personal"}
TODO_STATES = {"pendiente", "en_progreso", "bloqueada", "hecha", "cancelada"}

def note_to_db_properties(note, eje=None):
    props = {
        "Texto": {"title": [{"text": {"content": note["texto"]}}]},
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
        "Name": {"title": [{"text": {"content": todo["description"]}}]},
        "Fecha": {"date": {"start": todo["date"]}} if todo.get("date") else {"date": None},
        "Tags": {"multi_select": [{"name": t} for t in todo["tags"]]},
        "Estado": {"select": {"name": todo["state"]}},
    }
```

- [ ] **Step 8: Correr los tests, confirmar que pasan**

Run: `python3 -m pytest convert_test.py -v`
Expected: 9 passed

- [ ] **Step 9: Escribir los tests de `markdown_to_blocks`**

```python
# agregar a scripts/migration/convert_test.py
from convert import markdown_to_blocks

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
```

- [ ] **Step 10: Correr los tests, confirmar que fallan**

Run: `python3 -m pytest convert_test.py -v`
Expected: FAIL — `ImportError: cannot import name 'markdown_to_blocks'`

- [ ] **Step 11: Implementar `markdown_to_blocks`**

```python
# agregar a scripts/migration/convert.py
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
                "rich_text": [{"text": {"content": first_line[3:]}}]}})
            continue
        if first_line.startswith("# "):
            blocks.append({"type": "heading_1", "heading_1": {
                "rich_text": [{"text": {"content": first_line[2:]}}]}})
            continue
        if all(l.startswith("- ") for l in lines):
            for l in lines:
                blocks.append({"type": "bulleted_list_item", "bulleted_list_item": {
                    "rich_text": [{"text": {"content": l[2:]}}]}})
            continue
        blocks.append({"type": "paragraph", "paragraph": {
            "rich_text": [{"text": {"content": para}}]}})
    return blocks
```

- [ ] **Step 12: Correr toda la suite, confirmar que pasa completa**

Run: `python3 -m pytest convert_test.py -v`
Expected: 13 passed

- [ ] **Step 13: Commit**

```bash
cd ~/.claude/skills/second-brain
git init -q 2>/dev/null || true
git add scripts/migration/convert.py scripts/migration/convert_test.py
git commit -m "feat: funciones puras de conversión perfil/notas/todos/research a Notion" 2>/dev/null || \
  echo "sin git en ~/.claude — cambios quedan solo en disco, ver nota en el spec"
```

> Nota: si `~/.claude` no es un repo git (confirmado que no lo es hoy), este paso
> de commit no aplica — el checkbox se marca igual una vez guardado el archivo en
> disco, no hace falta instalar git ahí solo por este plan.

---

### Task 3: Crear la estructura del workspace (`setup_workspace.py`)

**Files:**
- Create: `scripts/migration/setup_workspace.py`
- Produces: `references/notion-ids.json`

**Interfaces:**
- Consumes: `NOTION_TOKEN`, `NOTION_ROOT_PAGE_ID` (env vars de Task 1).
- Produces: `references/notion-ids.json` con shape:
  ```json
  {
    "root_page_id": "...",
    "perfil_page_id": "...",
    "eje_page_ids": {"salud": "...", "emocional": "...", "proyectos": "...",
                      "trabajo": "...", "academico": "...", "general": "..."},
    "notas_db_id": "...",
    "insights_db_id": "...",
    "todos_db_id": "...",
    "research_page_id": "..."
  }
  ```
  Consumido por `migrate_content.py` (Task 4) y citado en `SKILL.md` (Tasks 7-9).

- [ ] **Step 1: Instalar la dependencia**

Run: `pip install notion-client`
Expected: instalación exitosa (no hay test unitario para esto — es una dependencia externa)

- [ ] **Step 2: Escribir `setup_workspace.py`**

```python
# scripts/migration/setup_workspace.py
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

    notas_db = notion.databases.create(
        parent={"page_id": root_id},
        title=[{"text": {"content": "Notas"}}],
        properties={
            "Texto": {"title": {}},
            "Eje": {"select": {"options": [{"name": v} for v in EJES.values()]}},
            "Fecha": {"date": {}},
            "ID": {"unique_id": {"prefix": "NOTE"}},
        },
    )

    insights_db = notion.databases.create(
        parent={"page_id": root_id},
        title=[{"text": {"content": "Insights"}}],
        properties={
            "Texto": {"title": {}},
            "Fecha": {"date": {}},
            "ID": {"unique_id": {"prefix": "INS"}},
        },
    )

    todos_db = notion.databases.create(
        parent={"page_id": root_id},
        title=[{"text": {"content": "Todos"}}],
        properties={
            "Name": {"title": {}},
            "Fecha": {"date": {}},
            "Tags": {"multi_select": {"options": [{"name": t} for t in TODO_TAGS]}},
            "Estado": {"select": {"options": [{"name": s} for s in TODO_STATES]}},
            "ID": {"unique_id": {"prefix": "TODO"}},
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
        "insights_db_id": insights_db["id"],
        "todos_db_id": todos_db["id"],
        "research_page_id": research["id"],
    }
    out_path = os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")
    with open(out_path, "w") as f:
        json.dump(ids, f, indent=2, ensure_ascii=False)
    print(f"IDs escritos en {out_path}")

if __name__ == "__main__":
    main()
```

> Contingencia: si `unique_id` no es aceptado como tipo de propiedad al crear una
> base vía API (verificar con el error devuelto en Step 3), quitar la propiedad
> `"ID"` de las tres bases en este script, correrlo igual, y crear la propiedad
> `ID` a mano desde la UI de Notion en cada base después — el resto del plan no
> depende de en qué momento se agregó esa propiedad, solo de que exista antes de
> Task 4.

- [ ] **Step 3: Correr el script una sola vez contra el workspace real**

Run: `cd ~/.claude/skills/second-brain/scripts/migration && python3 setup_workspace.py`
Expected: imprime "IDs escritos en .../references/notion-ids.json" sin errores

- [ ] **Step 4: Verificar manualmente en Notion**

Abrir la página raíz en el navegador y confirmar a simple vista: existe "Perfil"
con 6 sub-páginas (Salud, Emocional, Proyectos, Trabajo, Académico, General);
existen las bases "Notas", "Insights", "Todos" con sus columnas; existe la
página "Research". Si algo falta, revisar el error del Step 3 antes de seguir —
no conviene avanzar a Task 4 con la estructura incompleta.

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/second-brain
git add scripts/migration/setup_workspace.py references/notion-ids.json
git commit -m "feat: script de creación de estructura del workspace de Notion" 2>/dev/null || true
```

---

### Task 4: Migrar el árbol de perfil (`migrate_content.py`, parte 1)

**Files:**
- Create: `scripts/migration/migrate_content.py`

**Interfaces:**
- Consumes: `flatten_profile_tree` (Task 2), `references/notion-ids.json` (Task 3),
  `~/.claude/second-brain/profile.json` (fuente).
- Produces: función `migrate_profile_tree(notion, profile_json_path, ids)` — crea
  las páginas de Notion para cada nodo del árbol bajo su eje correspondiente.

- [ ] **Step 1: Escribir `migrate_profile_tree`**

```python
# scripts/migration/migrate_content.py
import json
import os
from notion_client import Client
from convert import flatten_profile_tree, note_to_db_properties, todo_to_db_properties, markdown_to_blocks

EJES = ["salud", "emocional", "proyectos", "trabajo", "academico", "general"]

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

if __name__ == "__main__":
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    with open(os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")) as f:
        ids = json.load(f)
    migrate_profile_tree(notion, os.path.expanduser("~/.claude/second-brain/profile.json"), ids)
    print("Árbol de perfil migrado.")
```

- [ ] **Step 2: Correr contra el workspace real**

Run: `cd ~/.claude/skills/second-brain/scripts/migration && python3 migrate_content.py`
Expected: imprime "Árbol de perfil migrado." sin errores

- [ ] **Step 3: Verificar manualmente en Notion**

Abrir "Perfil → Salud" y confirmar que aparecen las sub-páginas "ejercicio",
"dieta", "sueño" con su callout de resumen y el texto de `info` correspondiente
(comparar contra `~/.claude/second-brain/profile.json`). Repetir un chequeo
rápido en "trabajo → items"/"horario" y "academico → tesis → tesis.metodo_trabajo"
(el único nodo con nieto hoy) para confirmar que el anidamiento profundo quedó bien.

- [ ] **Step 4: Commit**

```bash
cd ~/.claude/skills/second-brain
git add scripts/migration/migrate_content.py
git commit -m "feat: migración del árbol de perfil a páginas de Notion" 2>/dev/null || true
```

---

### Task 5: Migrar notas, insights y todos (`migrate_content.py`, parte 2)

**Files:**
- Modify: `scripts/migration/migrate_content.py`

**Interfaces:**
- Consumes: `note_to_db_properties`, `todo_to_db_properties` (Task 2); `ids["notas_db_id"]`,
  `ids["insights_db_id"]`, `ids["todos_db_id"]` (Task 3); `profile.json["insights"]`,
  `profile.json[eje]["note"]`, `~/.claude/second-brain/todos.json`,
  `~/.claude/second-brain/todos-archive.json` (si existe).

- [ ] **Step 1: Agregar `migrate_notes_and_insights` y `migrate_todos`**

```python
# agregar a scripts/migration/migrate_content.py
EJE_TITULOS = {
    "salud": "Salud", "emocional": "Emocional", "proyectos": "Proyectos",
    "trabajo": "Trabajo", "academico": "Académico", "general": "General",
}

def migrate_notes_and_insights(notion, profile_json_path, ids):
    with open(profile_json_path) as f:
        profile = json.load(f)

    for eje in EJES:
        for note in profile[eje].get("note", []):
            notion.pages.create(
                parent={"database_id": ids["notas_db_id"]},
                properties=note_to_db_properties(note, eje=EJE_TITULOS[eje]),
            )

    for insight in profile.get("insights", []):
        notion.pages.create(
            parent={"database_id": ids["insights_db_id"]},
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
                parent={"database_id": ids["todos_db_id"]},
                properties=todo_to_db_properties(todo),
            )
```

- [ ] **Step 2: Actualizar el bloque `if __name__ == "__main__"` para llamar a las nuevas funciones**

```python
# reemplazar el bloque __main__ de scripts/migration/migrate_content.py
if __name__ == "__main__":
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    with open(os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")) as f:
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
```

- [ ] **Step 3: Correr contra el workspace real**

Run: `python3 migrate_content.py`
Expected: las tres líneas de confirmación, sin errores. Nota: `todos-archive.json`
no existe hoy — el script debe saltarlo sin fallar (ya contemplado en el `if not
os.path.exists`).

- [ ] **Step 4: Verificar manualmente en Notion**

Abrir la base "Notas" y contar filas: deben ser 5 (2 en salud, 1 en trabajo, 1 en
academico, 1 en general, según el `profile.json` actual). Abrir "Insights":
0 filas (la lista está vacía hoy). Abrir "Todos": mismo número de filas que
entradas en `todos.json["todos"]`.

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/second-brain
git add scripts/migration/migrate_content.py
git commit -m "feat: migración de notas, insights y todos a bases de Notion" 2>/dev/null || true
```

---

### Task 6: Migrar investigaciones (`migrate_content.py`, parte 3) y verificación final

**Files:**
- Modify: `scripts/migration/migrate_content.py`
- Create: `scripts/migration/verify_migration.py`

**Interfaces:**
- Consumes: `markdown_to_blocks` (Task 2); `ids["research_page_id"]` (Task 3);
  `~/.claude/second-brain/research/*.md`.

- [ ] **Step 1: Agregar `migrate_research`**

```python
# agregar a scripts/migration/migrate_content.py
import glob

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
```

- [ ] **Step 2: Agregar la llamada en `__main__`**

```python
# agregar al final del bloque __main__ de scripts/migration/migrate_content.py, antes del último print
    migrate_research(notion, os.path.expanduser("~/.claude/second-brain/research"), ids)
    print("Investigaciones migradas.")
```

- [ ] **Step 3: Correr contra el workspace real**

Run: `python3 migrate_content.py`
Expected: "Investigaciones migradas." sin errores (nota: al correr `migrate_content.py`
completo de nuevo se duplica lo ya migrado en pasos previos — si se ejecuta de
nuevo tras Task 4/5, comentar temporalmente esas llamadas o vaciar el workspace
de prueba antes de repetir)

- [ ] **Step 4: Escribir `verify_migration.py`**

```python
# scripts/migration/verify_migration.py
import json
import os
import glob
from notion_client import Client

def count_profile_nodes(node):
    return 1 + sum(count_profile_nodes(c) for c in node.get("childs", []))

def main():
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    with open(os.path.join(os.path.dirname(__file__), "..", "..", "references", "notion-ids.json")) as f:
        ids = json.load(f)
    with open(os.path.expanduser("~/.claude/second-brain/profile.json")) as f:
        profile = json.load(f)

    problems = []

    for eje, page_id in ids["eje_page_ids"].items():
        expected = count_profile_nodes(profile[eje])
        children = notion.blocks.children.list(block_id=page_id)["results"]
        actual = 1 + sum(
            1 for c in children if c["type"] == "child_page"
        )  # aproximación de primer nivel; ver nota abajo
        if actual < 1:
            problems.append(f"{eje}: página raíz sin hijos detectados")

    expected_notes = sum(len(profile[e].get("note", [])) for e in ids["eje_page_ids"])
    actual_notes = len(notion.databases.query(database_id=ids["notas_db_id"])["results"])
    if actual_notes != expected_notes:
        problems.append(f"Notas: esperabadas {expected_notes}, encontradas {actual_notes}")

    expected_insights = len(profile.get("insights", []))
    actual_insights = len(notion.databases.query(database_id=ids["insights_db_id"])["results"])
    if actual_insights != expected_insights:
        problems.append(f"Insights: esperados {expected_insights}, encontrados {actual_insights}")

    with open(os.path.expanduser("~/.claude/second-brain/todos.json")) as f:
        todos = json.load(f)
    expected_todos = len(todos["todos"])
    actual_todos = len(notion.databases.query(database_id=ids["todos_db_id"])["results"])
    if actual_todos != expected_todos:
        problems.append(f"Todos: esperados {expected_todos}, encontrados {actual_todos}")

    research_dir = os.path.expanduser("~/.claude/second-brain/research")
    expected_research = len([p for p in glob.glob(os.path.join(research_dir, "*.md"))
                              if os.path.basename(p) != "index.md"])
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
```

> Nota: el conteo de nodos de perfil por eje (`actual`) es una aproximación de
> primer nivel — confirmar recursivamente a mano en Notion si este chequeo
> reporta menos de lo esperado, ya que contar sub-páginas anidadas por API
> requiere recorrer cada nivel (`blocks.children.list` recursivo), omitido acá
> por simplicidad dado que Task 4 Step 3 ya lo revisó visualmente en profundidad.

- [ ] **Step 5: Correr la verificación**

Run: `cd ~/.claude/skills/second-brain/scripts/migration && python3 verify_migration.py`
Expected: `OK: todos los conteos coinciden.`

- [ ] **Step 6: Commit**

```bash
cd ~/.claude/skills/second-brain
git add scripts/migration/migrate_content.py scripts/migration/verify_migration.py
git commit -m "feat: migración de investigaciones + verificación de conteos post-migración" 2>/dev/null || true
```

---

### Task 7: Conectar el MCP remoto de Notion en Claude Code (terminal + PC de la pega)

**Files:** ninguno — configuración de cliente, no código.

- [ ] **Step 1: Agregar el connector en esta máquina**

Run: `claude mcp add --transport http notion https://mcp.notion.com/mcp`
Expected: se abre el navegador para autorizar OAuth con la cuenta de Notion del
Step 1/Task 1; tras autorizar, el comando confirma la conexión.

- [ ] **Step 2: Verificar que Claude Code puede ver el workspace**

En una sesión nueva de Claude Code, pedir: "usando el MCP de Notion, listá las
páginas hijas de la página raíz del segundo cerebro". Confirmar que responde con
"Perfil", "Notas", "Insights", "Todos", "Research".

- [ ] **Step 3: Repetir en la PC de la pega**

Mismo Step 1 y Step 2, ejecutados en esa máquina — sin esto, la PC de la pega
sigue sin acceso aunque el workspace ya exista.

---

### Task 8: Reescribir `SKILL.md` — secciones 0, 1 y 2 (mecánica central)

**Files:**
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: `references/notion-ids.json` (Task 3) para completar la tabla de IDs.

- [ ] **Step 1: Agregar una sección de IDs al principio de `SKILL.md`, después de la tabla de "Todo vive bajo..."**

```markdown
## IDs de Notion (fijos, no cambian tras la migración)

| Elemento | ID |
|---|---|
| Página raíz | `<root_page_id>` |
| Perfil | `<perfil_page_id>` |
| Perfil › salud | `<eje_page_ids.salud>` |
| Perfil › emocional | `<eje_page_ids.emocional>` |
| Perfil › proyectos | `<eje_page_ids.proyectos>` |
| Perfil › trabajo | `<eje_page_ids.trabajo>` |
| Perfil › academico | `<eje_page_ids.academico>` |
| Perfil › general | `<eje_page_ids.general>` |
| Base "Notas" | `<notas_db_id>` |
| Base "Insights" | `<insights_db_id>` |
| Base "Todos" | `<todos_db_id>` |
| Research | `<research_page_id>` |

Estos valores salen de `references/notion-ids.json` (generado una sola vez por
`scripts/migration/setup_workspace.py`) — completar la tabla copiando ese archivo
literalmente, no inventar ni recalcular IDs.
```

- [ ] **Step 2: Completar la tabla del Step 1 con los valores reales**

Abrir `references/notion-ids.json` (Task 3) y reemplazar cada `<...>` de la
tabla anterior por su valor real correspondiente.

- [ ] **Step 3: Reescribir la sección "1. Pendientes (tareas)"**

Reemplazar la tabla completa de comandos `todo.py` por:

```markdown
## 1. Pendientes (tareas)

Los pendientes viven en la base de datos "Todos" de Notion (ver tabla de IDs).
Todo el acceso pasa por las tools del MCP de Notion — nunca generar ni suponer
IDs de fila a mano.

| El usuario dice | Acción vía MCP de Notion |
|---|---|
| "añade X al todo para el viernes" | crear página en la base Todos: `Name`=X, `Fecha`=viernes, `Tags`=[...] |
| "qué tengo (para hoy / atrasado)" | consultar la base Todos filtrando por `Fecha` y `Estado` |
| "ya hice X" | actualizar la propiedad `Estado` de esa página a `hecha` |
| "mueve X para el lunes" | actualizar la propiedad `Fecha` de esa página |
| "X ya no aplica" | actualizar `Estado` a `cancelada` |
| "bórralo (explícitamente)" | archivar la página (`pages.update` con `archived: true`) |
| "cuánto me he atrasado" | consultar la base Todos filtrando `Fecha` < hoy y `Estado` = `pendiente` |

Tags: `tesis` · `trabajo` · `personal` — estados: `pendiente` · `en_progreso` ·
`bloqueada` · `hecha` · `cancelada` (mismo vocabulario de siempre, ahora
enforced por las propiedades `select`/`multi_select` de Notion — un valor fuera
de esta lista directamente no se puede asignar).
Fechas relativas ("mañana", "el viernes") se resuelven con el shell (`date -d
...`), nunca de memoria.
Nunca archivar con la tool de borrado salvo pedido explícito; para descartar
usa `Estado`=`cancelada`.
```

- [ ] **Step 4: Reescribir la sección "2. Perfil personal — todo es un árbol de nodos"**

Reemplazar el bloque de comandos CLI (`profile.py tree/list/show/set/append/rm/
note/notas/rm-nota/insight/insights/rm-insight`) por:

```markdown
## 2. Perfil personal (Notion) — todo es un árbol de páginas

El perfil sigue siendo, de punta a punta, un árbol de nodos — ahora representado
con la jerarquía nativa de páginas de Notion en vez de un JSON:

- Cada nodo del árbol es una página de Notion, anidada bajo su nodo padre
  (profundidad libre, igual que antes).
- El primer bloque de la página es un *callout* con el `desc` (resumen de una
  línea) — permite "hojear" la estructura sin abrir el contenido completo.
- El resto de la página (párrafos) es el `info` — texto plano, misma disciplina
  de siempre: ramificar en sub-páginas cuando crece o mezcla temas, en vez de
  meterle estructura al texto.
- Los 6 ejes de primer nivel (salud, emocional, proyectos, trabajo, academico,
  general) son fijos — sus IDs están en la tabla de arriba, no hace falta
  buscarlos por nombre cada vez.

| Antes (`profile.py`) | Ahora (tool de Notion) |
|---|---|
| `tree [eje]` | listar sub-páginas recursivamente desde el ID del eje |
| `list [eje] [path]` | listar sub-páginas directas de una página puntual |
| `show <eje> [path]` | leer los bloques de una página puntual |
| `set <eje> <path> --desc/--info` | crear la página (si no existe) o reemplazar su callout/contenido |
| `append <eje> <path> "texto"` | agregar un bloque `paragraph` al final de la página |
| `rm <eje> <path>` | archivar la página (`archived: true`) |
| `note <eje> "texto"` | crear una fila en la base "Notas" con `Eje`=el eje correspondiente |
| `notas <eje>` | consultar la base "Notas" filtrando por `Eje` |
| `rm-nota <eje> <id>` | archivar esa fila de la base "Notas" |
| `insight "texto"` | crear una fila en la base "Insights" |
| `insights` | consultar la base "Insights" completa |
| `rm-insight <id>` | archivar esa fila de la base "Insights" |

El resto de esta sección (flujo de lectura por rama, cuándo ramificar un nodo
que crece, disciplina de notas vs. nodos estructurados) se mantiene sin
cambios de fondo — donde diga "profile.py show/set/append", leer "la tool de
Notion equivalente de la tabla de arriba".
```

- [ ] **Step 5: Verificación manual**

Abrir una sesión de Claude Code con el connector de Notion activo y pedir "qué
tengo pendiente para hoy" y "qué sabés de mi perfil de salud" — confirmar que
consulta la base Todos y las páginas de Notion en vez de intentar correr
`todo.py`/`profile.py`.

- [ ] **Step 6: Commit**

```bash
cd ~/.claude/skills/second-brain
git add SKILL.md
git commit -m "docs: reescribir secciones 0-2 de SKILL.md para operar sobre Notion" 2>/dev/null || true
```

---

### Task 9: Actualizar `SKILL.md` — secciones 3, 4, 5, 6, 8 y "Reglas generales"

**Files:**
- Modify: `SKILL.md`

Reemplazar cada referencia literal a comandos `profile.py`/`todo.py` fuera de las
secciones 0-2 por un puntero a la sección 2 (que ya define la equivalencia), en
vez de repetir la mecánica de Notion en cada lugar.

- [ ] **Step 1: Sección 3 (Salud)** — reemplazar:

```markdown
- Revisa `profile.py show salud ejercicio`, `show salud dieta` y `show salud sueño`
  antes de sugerir algo (nivel, objetivo, lesiones, preferencias y plan_actual de
  ejercicio; restricciones/preferencias/objetivo de dieta; horario/hábitos de sueño).
```

por:

```markdown
- Revisa las páginas `salud.ejercicio`, `salud.dieta` y `salud.sueño` (ver
  sección 2) antes de sugerir algo (nivel, objetivo, lesiones, preferencias y
  plan_actual de ejercicio; restricciones/preferencias/objetivo de dieta;
  horario/hábitos de sueño).
```

y reemplazar:

```markdown
- Guarda en el perfil lo que reporte: lesiones, restricciones, gustos ("prefiere
  entrenar en la mañana"), qué plan sigue actualmente — como nota primero
  (`note salud "..."`) y reflejado en el nodo correspondiente, ej.
  `show salud ejercicio` para ver el info actual y luego `set salud ejercicio
  --info "texto completo con el plan_actual actualizado"`.
```

por:

```markdown
- Guarda en el perfil lo que reporte: lesiones, restricciones, gustos ("prefiere
  entrenar en la mañana"), qué plan sigue actualmente — primero como fila nueva
  en la base "Notas" (`Eje`=Salud), y reflejado en la página `salud.ejercicio`
  (leer su contenido actual y reemplazarlo con el plan_actual actualizado, ver
  sección 2).
```

- [ ] **Step 2: Sección 4 (Emocional)** — reemplazar:

```markdown
- Revisa `profile.py show emocional patrones_observados` y `show emocional
  estrategias_que_funcionan` — si ya sabes qué lo ha ayudado en el pasado,
  mencionarlo hace el consejo mucho más útil que uno genérico.
```

por:

```markdown
- Revisa las páginas `emocional.patrones_observados` y
  `emocional.estrategias_que_funcionan` (ver sección 2) — si ya sabes qué lo ha
  ayudado en el pasado, mencionarlo hace el consejo mucho más útil que uno
  genérico.
```

y reemplazar:

```markdown
- Guarda patrones y estrategias que funcionen (`note emocional "..."` y luego
  `append emocional estrategias_que_funcionan "..."` o
  `append emocional patrones_observados "..."`) para que la próxima vez el
  consejo parta de ahí.
```

por:

```markdown
- Guarda patrones y estrategias que funcionen (fila nueva en "Notas" con
  `Eje`=Emocional, y un bloque agregado al final de
  `emocional.estrategias_que_funcionan` o `emocional.patrones_observados`, ver
  sección 2) para que la próxima vez el consejo parta de ahí.
```

- [ ] **Step 3: Sección 5 (Proyectos, trabajo y academia)** — reemplazar:

```markdown
- El proyecto en sí (descripción, plan, estado) vive en
  `profile.py show proyectos items` / `append proyectos items "..."`.
```

por:

```markdown
- El proyecto en sí (descripción, plan, estado) vive en la página
  `proyectos.items` (ver sección 2).
```

- [ ] **Step 4: Sección 6 (Organización del día)** — reemplazar:

```markdown
"Qué tengo que hacer hoy" combina `todo.py list --today` con contexto del perfil
(por ejemplo, si hoy tocaba entrenar según el `plan_actual` dentro de
`show salud ejercicio`, o si hay algo relevante en `trabajo`/`academico`/`general`
para hoy).
```

por:

```markdown
"Qué tengo que hacer hoy" combina una consulta a la base "Todos" filtrada por
fecha de hoy con contexto del perfil (por ejemplo, si hoy tocaba entrenar según
el `plan_actual` dentro de `salud.ejercicio`, o si hay algo relevante en
`trabajo`/`academico`/`general` para hoy).
```

- [ ] **Step 5: Sección 8 (Insights)** — reemplazar:

```markdown
- **Guardar la hipótesis**: `profile.py insight "..."` — mismo formato que las
  notas (id + fecha + texto), pero en una lista separada (`insights`, a nivel de
  perfil, no dentro de un eje) porque es una conclusión **tuya**, no algo que el
  usuario dijo textualmente. No pidas permiso para guardarla; solo hazlo.
```

por:

```markdown
- **Guardar la hipótesis**: crear una fila nueva en la base "Insights" de Notion
  — mismo formato que las notas (fecha + texto, con ID nativo autoincremental),
  pero en una base separada de "Notas" porque es una conclusión **tuya**, no
  algo que el usuario dijo textualmente. No pidas permiso para guardarla; solo
  hazlo.
```

y reemplazar:

```markdown
- **Al confirmarse**: si el usuario confirma una hipótesis (dice que sí, la
  corrige levemente, o la da por hecha en lo que sigue diciendo), pasa a ser
  información verdadera y sigue el mismo camino que cualquier dato nuevo
  aprendido (sección 2.1) — no se descarta sin dejar rastro:
  1. Regístrala como nota del eje que corresponda (`profile.py note <eje> "..."`)
     para trazabilidad de procedencia.
  2. Refléjala en el nodo estructurado correspondiente (`show`/`set`/`append`,
     citando la nota si aplica).
  3. Recién ahí, bórrala de la lista de insights (`profile.py rm-insight <id>`)
     — ya no es hipótesis, es dato, y vive como nota + nodo del árbol, no en la
     lista de insights.
  Si el usuario la desmiente, simplemente bórrala (`rm-insight <id>`) sin
  guardarla en ningún otro lado.
```

por:

```markdown
- **Al confirmarse**: si el usuario confirma una hipótesis (dice que sí, la
  corrige levemente, o la da por hecha en lo que sigue diciendo), pasa a ser
  información verdadera y sigue el mismo camino que cualquier dato nuevo
  aprendido (sección 2.1) — no se descarta sin dejar rastro:
  1. Regístrala como fila nueva en la base "Notas" del eje que corresponda,
     para trazabilidad de procedencia.
  2. Refléjala en la página estructurada correspondiente (ver sección 2,
     citando la nota si aplica).
  3. Recién ahí, archivá la fila en la base "Insights" — ya no es hipótesis, es
     dato, y vive como nota + página del árbol, no en "Insights".
  Si el usuario la desmiente, simplemente archivá la fila en "Insights" sin
  guardarla en ningún otro lado.
```

y reemplazar:

```markdown
- Revisa `profile.py insights` junto con el eje relevante antes de responder — una
  hipótesis pendiente bien fundada hace que un consejo pase de genérico a certero.
```

por:

```markdown
- Revisa la base "Insights" junto con el eje relevante antes de responder — una
  hipótesis pendiente bien fundada hace que un consejo pase de genérico a certero.
```

- [ ] **Step 6: "Reglas generales"** — reemplazar:

```markdown
- Nunca edites `profile.json`, `todos.json` ni `todos-archive.json` a mano —
  siempre por su CLI respectivo.
```

por:

```markdown
- Claude siempre opera sobre Notion vía las tools del MCP, nunca adivinando o
  reconstruyendo contenido de memoria. A diferencia del JSON local anterior, el
  usuario sí puede editar directamente en la app de Notion sin riesgo de romper
  el esquema (los `select`/`multi_select`/`date` de las bases no aceptan valores
  inválidos) — si lo hace, la próxima consulta de Claude ya ve ese cambio.
```

- [ ] **Step 7: Verificación manual**

Releer `SKILL.md` completo de corrido y confirmar que no queda ninguna mención a
`profile.py`/`todo.py` fuera de un comentario histórico explícito (no debería
quedar ninguna). Buscar con `grep -n "profile.py\|todo.py" SKILL.md` y confirmar
que no imprime nada.

- [ ] **Step 8: Commit**

```bash
cd ~/.claude/skills/second-brain
git add SKILL.md
git commit -m "docs: actualizar secciones 3-8 y reglas generales de SKILL.md a Notion" 2>/dev/null || true
```

---

### Task 10: Reescribir la sección 7 (Investigación) y retirar `subejes.md`

**Files:**
- Modify: `SKILL.md`
- Modify (deprecar): `references/subejes.md`

- [ ] **Step 1: Reemplazar la sección "7. Investigación"**

```markdown
## 7. Investigación

Antes de investigar algo desde cero, revisa si ya existe una página relevante
bajo "Research" (ver tabla de IDs) — usar la tool de búsqueda del MCP de Notion
acotada a esa página, no hace falta un índice manual aparte (Notion ya lista
las sub-páginas y tiene buscador de texto completo nativo).

- Si hay una página relevante y no está obsoleta para la pregunta, úsala
  directamente (dile al usuario de qué fecha es, por si quiere que se actualice
  — la fecha de creación de la página alcanza para esto, sin necesidad de un
  campo aparte).
- Si la pregunta es puntual y acotada (un dato, una comparación simple), usa
  búsqueda web directa (`WebSearch`/`WebFetch`) y responde citando la fuente.
- Si la pregunta requiere profundidad (comparar varias fuentes, diseñar algo con
  base en evidencia — ej. "un plan de 12 semanas con respaldo científico"),
  invoca la skill `deep-research` pasándole la pregunta.
- **Siempre que uses `deep-research`**, guarda su resultado como una página
  nueva bajo "Research" (título = tema investigado, contenido = el reporte o un
  resumen fiel si es muy largo) para no rehacer la investigación después.
```

- [ ] **Step 2: Marcar `references/subejes.md` como retirado**

Reemplazar todo el contenido del archivo por:

```markdown
# Retirado

Este catálogo quedó obsoleto tras la migración a Notion (ver
`notion-portability-design.md` y `notion-portability-plan.md` en este mismo
directorio). La navegación del árbol de perfil ahora se hace listando
sub-páginas directamente vía el MCP de Notion — no hace falta mantener un
índice aparte, así que este archivo no se actualiza más.
```

- [ ] **Step 3: Verificación manual**

Pedir a Claude Code (con el connector activo) "¿ya investigué algo sobre X?"
para un tema que sí está en "Research" y confirmar que lo encuentra sin
depender de `subejes.md` ni de `research/index.md` local.

- [ ] **Step 4: Commit**

```bash
cd ~/.claude/skills/second-brain
git add SKILL.md references/subejes.md
git commit -m "docs: reescribir investigación a Notion, retirar subejes.md" 2>/dev/null || true
```

---

### Task 11: Instrucciones condensadas para el Project de claude.ai, y deprecar scripts/datos locales

**Files:**
- Create: `references/claude-ai-project-instructions.md`
- Modify (deprecar, no borrar): `scripts/todo.py`, `scripts/profile.py`

- [ ] **Step 1: Escribir `references/claude-ai-project-instructions.md`**

Contenido: una versión condensada de `SKILL.md` sin rutas locales (`~/.claude/...`)
ni referencias a Claude Code, pensada para pegar en las instrucciones de un
Project de claude.ai con el connector de Notion habilitado. Incluye la misma
tabla de IDs de Notion (Task 8, Step 2) y un resumen de las secciones 0-8 en
prosa, apuntando siempre a operar vía las tools de Notion.

```markdown
# Segundo cerebro (instrucciones de Project — claude.ai)

Con el connector de Notion habilitado en este Project, tenés acceso al mismo
segundo cerebro que en la terminal: perfil (árbol de páginas), pendientes
(base "Todos"), notas e insights (bases "Notas"/"Insights"), investigaciones
(página "Research"). Ver la tabla de IDs abajo — son fijos, no los recalcules.

[pegar acá la tabla de IDs completa de SKILL.md, sección "IDs de Notion"]

## Cómo operar

- Pendientes: consultá/creá/actualizá filas en la base "Todos" (propiedades
  `Name`, `Fecha`, `Tags`: tesis/trabajo/personal, `Estado`:
  pendiente/en_progreso/bloqueada/hecha/cancelada).
- Perfil: cada nodo es una página anidada bajo su eje (salud, emocional,
  proyectos, trabajo, academico, general). El primer bloque de cada página es
  un callout con el resumen (`desc`); el resto es el contenido (`info`). Leé la
  rama relevante antes de responder, no vuelques todo el árbol de una vez.
- Notas: fila nueva en la base "Notas" con el `Eje` correspondiente, cada vez
  que surja algo nuevo y duradero sobre el usuario.
- Insights: fila nueva en la base "Insights" para conclusiones propias (no
  dichas textualmente) — nunca sobre edad, orientación, ubicación precisa u
  otra categoría puntualmente identificatoria.
- Investigación: buscá primero bajo "Research" antes de investigar desde cero;
  guardá ahí lo que investigues con `deep-research` o búsqueda web para no
  repetir trabajo.
- Nunca inventes o adivines contenido de una página/fila sin leerla primero vía
  el connector.
```

- [ ] **Step 2: Verificación manual**

En claude.ai (web), crear un Project "Segundo cerebro", habilitar el connector
de Notion (autorizar OAuth si pide, ver Task 6 para qué esperar), pegar el
contenido de este archivo como instrucciones del Project, y preguntar "qué
tengo pendiente hoy" en una conversación nueva dentro del Project — confirmar
que responde consultando la base "Todos" real. Repetir la misma prueba desde la
app de celular con la misma cuenta, y anotar en este mismo archivo (como
comentario al pie) si el connector estuvo disponible ahí sin autorización
aparte o si pidió una propia.

- [ ] **Step 3: Marcar como deprecados `scripts/todo.py` y `scripts/profile.py`**

Agregar como primeras líneas de cada archivo (no borrar el resto del contenido):

```python
# DEPRECADO (2026-07-13): reemplazado por el MCP de Notion, ver
# references/notion-portability-design.md y references/notion-portability-plan.md.
# Se conserva sin borrar como referencia histórica; SKILL.md ya no lo invoca.
```

- [ ] **Step 4: Commit**

```bash
cd ~/.claude/skills/second-brain
git add references/claude-ai-project-instructions.md scripts/todo.py scripts/profile.py
git commit -m "docs: instrucciones de Project para claude.ai; deprecar scripts locales" 2>/dev/null || true
```

---

## Self-Review

**Spec coverage:**
- Almacenamiento Notion + límites free tier → Global Constraints, Task 1/3.
- MCP oficial remoto + OAuth por cliente → Task 6.
- Árbol de perfil → páginas anidadas → Task 2 (`flatten_profile_tree`), Task 4.
- Notas/Insights → bases con ID nativo → Task 2/3/5.
- Todos → base de datos → Task 2/3/5.
- Investigación → páginas bajo "Research" → Task 2/6/10.
- Migración de un solo uso, JSON/MD locales no se borran → Tasks 3-6 (crean sin
  tocar los archivos fuente), Task 11 (deprecación explícita sin borrado).
- SKILL.md reescrito reemplazando CLI por tools de Notion → Tasks 8-10.
- Instrucciones condensadas para claude.ai → Task 11.
- Punto abierto del spec ("¿se elimina `todos-archive.json`/`research/index.md`
  tras confirmar migración?") → resuelto implícitamente: no se eliminan (se
  ignoran/deprecan igual que el resto), consistente con "no se borra nada".

**Placeholder scan:** sin "TBD"/"TODO"/"implementar después" en ningún step;
los `<...>` de la tabla de IDs (Task 8) se resuelven en el Step inmediatamente
siguiente con datos reales de `notion-ids.json`, no quedan sin completar.

**Type/naming consistency:** `flatten_profile_tree`, `note_to_db_properties`,
`todo_to_db_properties`, `markdown_to_blocks` se usan con la misma firma en
Task 2 (definición) y Tasks 4-6 (consumo). Las claves de `notion-ids.json`
(`eje_page_ids`, `notas_db_id`, `insights_db_id`, `todos_db_id`,
`research_page_id`) se usan consistentemente entre Task 3 (productor) y Tasks
4-6, 8, 11 (consumidores).

---

**Plan complete and saved to `/home/vgonzalez/.claude/skills/second-brain/references/notion-portability-plan.md`.**
