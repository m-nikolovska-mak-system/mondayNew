<div align="center">

# 🚀 Assign Jira Issue

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/assign-jira-issue.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `assign`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Install jq and python3

```bash
sudo apt-get update -y
sudo apt-get install -y jq python3
```

#### 2. Assign issue in Jira

```bash
set -e
if [ -z "$JIRA_EMAIL" ] || [ -z "$JIRA_API_TOKEN" ] || [ -z "$JIRA_URL" ]; then
  echo "Missing Jira secrets: JIRA_EMAIL, JIRA_API_TOKEN, JIRA_URL"
  exit 1
fi
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
