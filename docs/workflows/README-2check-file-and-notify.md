# 📝 Detect File Changes + Notify Teams

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/2check-file-and-notify.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check_changes`

**Runner:** `unknown`

**Steps:**

### `debug_print`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - 💻 Run: `echo "changed files:  ${{ needs.check_changes.outputs.changed_files_list }}" echo "all changed:    ${{ needs.check_chang...`

### `notify_if_changed`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
