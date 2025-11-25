# 📝 Detect File Change + MS Teams Notification Workflow

## Overview

**Workflow Name:** `Detect File Change + MS Teams Notification`

## Triggers


## Jobs

### `check_changes`

### `debug_print`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Show outputs**
   - Runs: `echo "files_changed='${{ needs.check_changes.outputs.files_c...`

### `notify_if_changed`

---

*This documentation is auto-generated. Do not edit manually.*
