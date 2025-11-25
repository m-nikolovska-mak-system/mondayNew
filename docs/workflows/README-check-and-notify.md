# 📝 Detect File Change + MS Teams Notification

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/check-and-notify.yml`

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

1. **Show outputs**
   - 💻 Run: `echo "files_changed='${{ needs.check_changes.outputs.files_changed }}'" echo "changed_files_list='${{ needs.check_change...`

### `notify_if_changed`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
