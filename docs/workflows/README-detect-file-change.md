# 📝 Detect File Change

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/detect-file-change.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `detect`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `found`: `${{ steps.result.outputs.found }}`
- `files`: `${{ steps.result.outputs.files }}`

**Steps:**

1. **Step 1**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`

2. **Detect changed files**
   - 💻 Run: `set -e AFTER="${{ github.event.release.tag_name }}" WATCHED_PATH="${{ inputs.watched_path }}"  git fetch --tags --quiet ...`

---

*This documentation is auto-generated. Do not edit manually.*
