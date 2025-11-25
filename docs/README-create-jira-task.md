<div align="center">

# 🚀 Create Jira Task on App Change

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/create-jira-task.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `create-jira`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repository (full)

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 0
```

#### 2. Gather changed files

```bash
# If this is the first push (no before SHA) list all files in the commit
if [ "${{ github.event.before }}" = "0000000000000000000000000000000000000000" ]; then
  echo "Initial commit or branch created - listing files in ${GITHUB_SHA}"
  git ls-tree -r --name-only ${GITHUB_SHA} > files.txt
  CHANGED=$(cat files.txt)
# ... (truncated)
```

#### 3. Check for app file changes

```bash
FILES="${{ steps.changes.outputs.files }}"
echo "Changed files:\n$FILES"
if echo "$FILES" | grep -qE 'com/miha/app/'; then
  echo "found=true" >> $GITHUB_OUTPUT
else
# ... (truncated)
```

#### 4. Create Jira issue when app files changed

```bash
set -e
# Basic validation of required secrets
if [ -z "$JIRA_EMAIL" ] || [ -z "$JIRA_API_TOKEN" ] || [ -z "$JIRA_URL" ] || [ -z "$JIRA_PROJECT_KEY" ]; then
  echo "Missing one of required secrets: JIRA_EMAIL, JIRA_API_TOKEN, JIRA_URL, JIRA_PROJECT_KEY"
  exit 1
# ... (truncated)
```

#### 5. Upload created issue metadata

```yaml
uses: actions/upload-artifact@v4
with:
  name: jira-issue-info
  path: issue_info.txt
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
