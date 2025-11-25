# 📝 Generate Workflow Docs Workflow

## Overview

**Workflow Name:** `Generate Workflow Docs`

## Triggers


## Jobs

### `build-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - Uses: `actions/checkout@v4`
2. **Ensure output directory exists**
   - Runs: `mkdir -p $(dirname "${{ github.event.inputs.output }}")...`
3. **Generate README with auto-doc**
   - Uses: `tj-actions/auto-doc@v3`
4. **Debug git status**
   - Runs: `git status --short...`
5. **Commit generated docs**
   - Uses: `EndBug/add-and-commit@v9`

---

*This documentation is auto-generated. Do not edit manually.*
