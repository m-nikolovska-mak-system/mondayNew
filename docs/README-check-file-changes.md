# 📝 Check File Changes Workflow

## Overview

**Workflow Name:** `Check File Changes`

## Triggers


## Jobs

### `check`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - Uses: `actions/checkout@v4`
2. **Resolve refs**
   - Runs: `current="${{ inputs.current_ref }}"...`
3. **Detect changes**
   - Runs: `pattern="${{ inputs.file_pattern }}"...`

---

*This documentation is auto-generated. Do not edit manually.*
