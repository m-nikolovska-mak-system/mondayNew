# 📝 Simple README Generator Workflow

## Overview

**Workflow Name:** `Simple README Generator`

## Triggers


## Jobs

### `generate-readme`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - Uses: `actions/checkout@v4`
2. **Select workflow file**
   - Runs: `echo "workflow_file=.github/workflows/build-installer.yml" >...`
3. **Ensure docs folder exists**
   - Runs: `mkdir -p docs...`
4. **Prepare initial README if needed**
   - Runs: `FILE=docs/README-${{ steps.select.outputs.basename }}.md...`
5. **Run auto-doc**
   - Uses: `tj-actions/auto-doc@v3`
6. **Commit README changes**
   - Uses: `stefanzweifel/git-auto-commit-action@v5`
7. **Show result**
   - Runs: `echo "==== README OUTPUT ===="...`

---

*This documentation is auto-generated. Do not edit manually.*
