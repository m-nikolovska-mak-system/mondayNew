# 📝 Branch Name Check Workflow

## Overview

**Workflow Name:** `Branch Name Check`

## Triggers


## Jobs

### `check-branch`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - Uses: `actions/checkout@v4`
2. **Get branch name**
   - Runs: `# Try multiple methods to get branch name...`
3. **Check branch naming convention**
   - Runs: `branch="${{ steps.branch.outputs.branch }}"...`
4. **Additional branch checks**
   - Runs: `branch="${{ steps.branch.outputs.branch }}"...`

---

*This documentation is auto-generated. Do not edit manually.*
