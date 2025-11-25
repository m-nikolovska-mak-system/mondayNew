# 📝 Notify on App.java Changes

**Generated:** 2025-11-25 14:06:40 UTC

---

## Overview

**Workflow File:** `.github/workflows/notify-app-changes-v3.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check-file-changes`

**Runner:** `unknown`

**Steps:**

### `debug-outputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Print check results**
   - 💻 Run: `echo "Job status: ${{ needs.check-file-changes.result }}" echo "Files changed: ${{ needs.check-file-changes.outputs.file...`

### `send-teams-notification`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
