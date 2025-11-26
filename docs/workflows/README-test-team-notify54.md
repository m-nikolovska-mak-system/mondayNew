# 📝 Notify Teams on Changes

**Generated:** 2025-11-26 12:27:54 UTC

---

## Overview

**Workflow File:** `.github/workflows/test-team-notify54.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `detect-changes`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `changed_files`: `${{ steps.changes.outputs.files }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `2`

2. **Get changed files**
   - 💻 Run: `# For push events, compare with previous commit if [ "${{ github.event_name }}" = "push" ]; then   FILES=$(git diff --na...`

### `notify-teams`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
