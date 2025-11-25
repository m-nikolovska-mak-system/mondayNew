<div align="center">

# 🚀 Teams Notification Template THIS IS THE GOOD ONE

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/testNotif2.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `send-notification`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repository

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 0
```

#### 2. Detect changed files

```bash
set -e
echo "🔍 Detecting changed files..."

if [ "${{ github.event.before }}" = "0000000000000000000000000000000000000000" ]; then
  echo "📦 Initial commit detected — listing all files in ${GITHUB_SHA}"
# ... (truncated)
```

#### 3. Send Microsoft Teams notification

```bash
set -e

# Validate webhook URL
if [ -z "$TEAMS_WEBHOOK_URL" ]; then
  echo "❌ Missing teams_webhook_url secret."
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
