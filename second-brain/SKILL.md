---
name: second-brain
description: Personal memory and task system backed by a private Git repository. Use for todos, durable preferences, health or emotional context, projects, work, academics, research, or whenever a user statement or decision could benefit from stored context. Activate lightly to capture durable facts without taking over the primary task.
---

# Second Brain

Use the private repository `git@github.com:Seivier/SecondBrain.git` as the only source of truth. Its clone location is fixed:

- Linux/macOS: `~/SecondBrain`
- Windows: `%USERPROFILE%\\SecondBrain`

## Prepare the repository

Before any read or write, resolve the platform path. If absent, clone the repository there. If present, verify `origin` is exactly the configured repository, then fast-forward from `origin/master`. Never create or use another clone. Stop and report a dirty clone, a mismatched remote, merge conflict, or authentication failure.

Read `MEMORY.md`, then request the smallest useful context:

```bash
python3 scripts/brain.py context --axis <axis> [--topic <topic>]
```

Open only the returned wiki pages. Use `scripts/brain.py` for todos, notes and insights; never open or edit `data/*.json` directly.

## Activation and capture

- **Full mode:** use for requests about todos, health, emotional support, projects, work, academics or research. Read only the relevant branch and filtered records before answering.
- **Light mode:** activate during any task when the user explicitly gives a stable preference, constraint, recurring routine, enduring goal or durable project fact. Capture it, then continue the original task without discussing the brain unless relevant.
- Do not save transient details, credentials, names, precise locations, employers, universities, third-party identifiers, or sensitive inferences. Health and emotional facts require a clear user statement; do not diagnose.
- A non-sensitive inference needs corroborating signals and is saved only as a pending insight. Promote it only after the user confirms it: add a note, update the wiki, then mark the insight `confirmado`.

## Writes and synchronization

Capture every durable fact as a note before adding it to the wiki. Every factual wiki bullet and `summary` needs `[note:NOTE-n]` or `[research:slug]`; use `sources` for summary provenance and keep `childs` aligned with direct children.

Mutating `brain.py` commands automatically fast-forward, validate, render, commit and push. After any direct wiki edit, immediately run:

```bash
python3 scripts/sync.py --message "brain: <concise change>"
```

If validation, commit or push fails, preserve the local change and report that it was not synchronized. Do not claim persistence until the push succeeds.

## Surface limits

Codex and Claude use the local clone and can write. ChatGPT without a writable authenticated clone is read-only: start with `views/mobile-brief.md`, then `MEMORY.md`, and identify durable facts for the next writable session rather than claiming to save them.
