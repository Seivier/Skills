---
name: second-brain
description: Personal memory and task system backed by a private Git repository. Use for todos, durable preferences, health or emotional context, projects, work, academics, research, or whenever a user statement or decision could benefit from stored context. Activate lightly to capture durable facts without taking over the primary task.
---

# Second Brain

Use the private repository `git@github.com:Seivier/SecondBrain.git` as the only source of truth. Its clone location is fixed:

- Linux/macOS: `~/SecondBrain`
- Windows: `%USERPROFILE%\\SecondBrain`

## Prepare the repository

Before any read or write, resolve the platform path. If absent, clone the repository there. If present, verify `origin` is exactly the configured repository, then fast-forward from `origin/master`. Never create or use another clone. Stop and report a dirty clone, mismatched remote, merge conflict or authentication failure.

Read `MEMORY.md`, then request the smallest useful context with one selector:

```bash
python3 scripts/brain.py context --page <page-or-stem>
python3 scripts/brain.py context --query <text>
```

Open only the returned wiki pages. Use `scripts/brain.py` for todos, notes and insights; never open or edit `data/*.json` directly.

## Activation and capture

- **Full mode:** use for requests about todos, health, emotional support, projects, work, academics or research. Read only the relevant branch and filtered records before answering.
- **Light mode:** activate when the user explicitly gives a stable preference, constraint, recurring routine, enduring goal or durable project fact. Capture it, then continue the original task without discussing the brain unless relevant.
- Do not save transient details, credentials, names, precise locations, employers, universities, third-party identifiers or sensitive inferences. Health and emotional facts require a clear user statement; do not diagnose.
- A non-sensitive inference needs corroborating signals and remains a pending insight until the user confirms it. After confirmation, capture the user's statement, update the wiki and mark the insight `confirmado`.

## Route knowledge through the tree

The wiki is the sole source of curated knowledge. It uses flat, hierarchically numbered Markdown files, while YAML frontmatter defines the semantic tree rooted at `wiki/0.index.md`.

1. Inspect titles and summaries to find the most specific existing branch.
2. Update the relevant leaf, or create a leaf under the most specific suitable parent.
3. Use General only when the information does not fit anywhere else in the current tree.
4. Write the result as if the user wrote it. Use first person where natural. Never say “the user indicated”, and never turn an assistant inference or recommendation into the user's belief.

Every page has a single H1 exactly equal to `title` and exactly one structural field:

```yaml
---
title: Parent topic
contents:
  - 1.topic.1.child.md
---
```

```yaml
---
title: Leaf topic
summary: A concise description of the knowledge contained in this leaf.
---
```

Parent pages have `contents` and no `summary`. Leaf pages have `summary` and no `contents`. Summaries must be nonempty, at most 1024 characters and contain neither `<` nor `>`. The body holds the leaf's actual knowledge or useful introductory prose for a parent.

Every page must have manual Markdown navigation immediately after its H1, with only the normal blank line between them. A parent duplicates `contents`:

```markdown
# Parent topic

## Contenidos

- [Child title](1.topic.1.child.md)
```

Parent link labels must exactly match each child's `title`; targets and order must exactly match YAML `contents`. Update both representations in the same edit whenever a child is inserted, renamed, moved, reordered or removed.

In a leaf, `## Contenidos` is an internal TOC that links every later H2-H6:

```markdown
# Leaf topic

## Contenidos

- [First section](#first-section)
  - [Nested section](#nested-section)

## First section

### Nested section
```

Labels and order must exactly match the headings. Targets use their lowercase Markdown anchors, preserving Unicode letters, removing punctuation and replacing spaces with hyphens. Indent nested headings by two spaces per level relative to H2. Every leaf must have at least one content heading. Update the TOC in the same edit whenever a heading is added, renamed, moved, re-leveled or removed. Do not use the obsolete `## Catálogo` heading.

Mirror the tree in every filename so filesystem sorting preserves reading order:

- The root is `0.index.md`.
- A root branch starts with its position and slug, such as `1.tesis`.
- Every branch index appends `.0.index.md`, such as `1.tesis.0.index.md`.
- Every child appends its position and slug, such as `1.tesis.1.tema.md`.
- A nested branch follows the same rule, for example `1.tesis.2.metodo.0.index.md` and `1.tesis.2.metodo.1.habitos.md`.
- Positions in `contents` start at 1, are contiguous and match the filenames in declared order.

When inserting, removing or moving a sibling, renumber that sibling set and every affected descendant so their prefixes continue to mirror the tree. Use `context --page` with a title or logical slug for normal reads; physical names remain accepted when exact targeting is useful.

## Reorganize only when a limit is crossed

A regular parent may have at most five children. The page titled General may have at most ten, and its direct children must all be leaves.

When an addition makes a regular parent exceed its limit, inspect only that parent and its children. Group related siblings beneath a well-named intermediate parent in the same branch, moving the minimum pages necessary, then renumber the affected sibling set and descendants. Parent names and nesting depth are chosen from the actual content; there are no mandatory categories.

When General exceeds ten children, inspect its leaves more deeply and consult only nearby branches that are plausible destinations. Move leaves into an existing specific branch or create a suitable topic when warranted, preserving the numbering convention in every affected branch. Keep the change minimal; do not scan or reorganize the whole wiki.

## Keep notes as audit history

Notes are not knowledge and are not provenance for wiki text. They are an independent history for the user to review possible hallucinations manually. When authorized to persist a durable statement, preserve the user's wording as literally as practical and record the wiki page and action:

```bash
python3 scripts/brain.py notes add "<user statement>" --page <numbered-file.md> --action <created|updated|moved>
```

Do not cite notes from the wiki. Git history audits structural reorganizations. Insights use a free topic rather than a fixed axis:

```bash
python3 scripts/brain.py insights add <topic> "<inference>"
```

## Synchronize

Mutating `brain.py` commands automatically fast-forward, validate, render, commit and push. After any direct wiki edit, immediately run:

```bash
python3 scripts/sync.py --message "brain: <concise change>"
```

If validation, commit or push fails, preserve the local change and report that it was not synchronized. Do not claim persistence until the push succeeds.

## Surface limits

Codex and Claude use the local clone and can write. ChatGPT without a writable authenticated clone is read-only: start with `views/mobile-brief.md`, then `MEMORY.md`, and identify durable facts for the next writable session rather than claiming to save them.
