<div align="center">

# 🚀 Test Teams Notification

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/test-teams-notif.yml`

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

#### 1. Send test Microsoft Teams notification

```bash
PAYLOAD='{"text": "Hello from act! This is a test notification."}'

echo "📤 Sending notification to Teams..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -H "Content-Type: application/json" -d "$PAYLOAD" "$TEAMS_WEBHOOK_URL")
if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "202" ]; then
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
