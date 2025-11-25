# 📝 Notify on App.java Changes Workflow

## Overview

**Workflow Name:** `Notify on App.java Changes`

## Triggers


## Jobs

### `check-file-changes`

### `debug-outputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Print check results**
   - Runs: `echo "Job status: ${{ needs.check-file-changes.result }}"...`

### `send-teams-notification`

---

*This documentation is auto-generated. Do not edit manually.*
