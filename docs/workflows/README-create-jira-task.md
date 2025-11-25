# 📝 Create Jira Task on App Change

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/create-jira-task.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `create-jira`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository (full)**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`

2. **Gather changed files**
   - 💻 Run: `# If this is the first push (no before SHA) list all files in the commit if [ "${{ github.event.before }}" = "0000000000...`

3. **Check for app file changes**
   - 💻 Run: `FILES="${{ steps.changes.outputs.files }}" echo "Changed files:\n$FILES" if echo "$FILES" | grep -qE 'com/miha/app/'; th...`

4. **Create Jira issue when app files changed**
   - 💻 Run: `set -e # Basic validation of required secrets if [ -z "$JIRA_EMAIL" ] || [ -z "$JIRA_API_TOKEN" ] || [ -z "$JIRA_URL" ] ...`

5. **Upload created issue metadata**
   - 📦 Action: `actions/upload-artifact@v4`
   - ⚙️ Config:
     - `name`: `jira-issue-info`
     - `path`: `issue_info.txt`

---

*This documentation is auto-generated. Do not edit manually.*
