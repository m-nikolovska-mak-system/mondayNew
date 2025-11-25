# 📝 🧩 Detect & Act on File Changes

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/check-file-changes5.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check_changes`

**Runner:** `unknown`

**Steps:**

### `run_on_change`

**Runner:** `ubuntu-latest`

**Steps:**

1. **✅ Files changed**
   - 💻 Run: `echo "Changed files:" echo "${{ needs.check_changes.outputs.changed_files_list }}" # Add your logic below (tests, build,...`

### `run_on_no_change`

**Runner:** `ubuntu-latest`

**Steps:**

1. **ℹ️ No watched files changed**
   - 💻 Run: `echo "No relevant files changed. Skipping build."...`

---

*This documentation is auto-generated. Do not edit manually.*
