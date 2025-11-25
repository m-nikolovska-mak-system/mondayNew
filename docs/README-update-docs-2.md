# 📝 Update Docs for Workflows Workflow

## Overview

**Workflow Name:** `Update Docs for Workflows`

## Triggers


## Jobs

### `update-docs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - Uses: `actions/checkout@v4`
2. **Generate docs for main action**
   - Uses: `tj-actions/auto-doc@v3`
3. **Generate docs for reusable workflow**
   - Uses: `tj-actions/auto-doc@v3`

---

*This documentation is auto-generated. Do not edit manually.*
