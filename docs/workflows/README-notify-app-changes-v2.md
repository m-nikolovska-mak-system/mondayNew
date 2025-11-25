# 📝 Notify on App.java Changes

**Generated:** 2025-11-25 14:06:40 UTC

---

## Overview

**Workflow File:** `.github/workflows/notify-app-changes-v2.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check_file_changes`

**Runner:** `unknown`

**Steps:**

### `debug_outputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Print outputs from check_file_changes**
   - 💻 Run: `echo "Files changed: ${{ needs.check_file_changes.outputs.files_changed }}" echo "Changed files list: ${{ needs.check_fi...`

### `send_teams_notification`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
