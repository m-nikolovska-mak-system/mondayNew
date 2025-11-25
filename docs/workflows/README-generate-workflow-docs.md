# 📝 Generate Workflow Docs

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/generate-workflow-docs.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `build-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - 📦 Action: `actions/checkout@v4`

2. **Ensure output directory exists**
   - 💻 Run: `mkdir -p $(dirname "${{ github.event.inputs.output }}")...`

3. **Generate README with auto-doc**
   - 📦 Action: `tj-actions/auto-doc@v3`
   - ⚙️ Config:
     - `filename`: `${{ github.event.inputs.filename }}`
     - `output`: `${{ github.event.inputs.output }}`

4. **Debug git status**
   - 💻 Run: `git status --short...`

5. **Commit generated docs**
   - 📦 Action: `EndBug/add-and-commit@v9`
   - ⚙️ Config:
     - `author_name`: `github-actions[bot]`
     - `author_email`: `41898282+github-actions[bot]@users.noreply.github.com`
     - `message`: `chore(docs): update workflow docs`
     - `add`: `.`
     - `push`: `True`
     - `allow_empty_commit`: `True`

---

*This documentation is auto-generated. Do not edit manually.*
