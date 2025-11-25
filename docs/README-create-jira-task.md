# 📝 Create Jira Task on App Change Workflow

## Overview

**Workflow Name:** `Create Jira Task on App Change`

## Triggers


## Jobs

### `create-jira`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository (full)**
   - Uses: `actions/checkout@v4`
2. **Gather changed files**
   - Runs: `# If this is the first push (no before SHA) list all files i...`
3. **Check for app file changes**
   - Runs: `FILES="${{ steps.changes.outputs.files }}"...`
4. **Create Jira issue when app files changed**
   - Runs: `set -e...`
5. **Upload created issue metadata**
   - Uses: `actions/upload-artifact@v4`

---

*This documentation is auto-generated. Do not edit manually.*
