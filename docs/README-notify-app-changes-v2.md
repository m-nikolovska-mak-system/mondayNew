# 📝 Notify on App.java Changes Workflow

## Overview

**Workflow Name:** `Notify on App.java Changes`

## Triggers


## Jobs

### `check_file_changes`

### `debug_outputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Print outputs from check_file_changes**
   - Runs: `echo "Files changed: ${{ needs.check_file_changes.outputs.fi...`

### `send_teams_notification`

---

*This documentation is auto-generated. Do not edit manually.*
