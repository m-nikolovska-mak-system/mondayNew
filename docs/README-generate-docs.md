# 📝 Generate workflow docs Workflow

## Overview

**Workflow Name:** `Generate workflow docs`

## Triggers


## Jobs

### `build-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repo**
   - Uses: `actions/checkout@v4`
2. **Generate README with auto-doc**
   - Uses: `tj-actions/auto-doc@v3`
3. **Commit generated docs**
   - Uses: `EndBug/add-and-commit@v9`

---

*This documentation is auto-generated. Do not edit manually.*
