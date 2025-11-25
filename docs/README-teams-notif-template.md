<div align="center">

# 🚀 Teams Notification Template

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/teams-notif-template.yml`

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
```

#### 2. Make script executable

```bash
chmod +x ./scripts/send-teams-notification.sh
```

#### 3. Send Microsoft Teams notification

```bash
./scripts/send-teams-notification.sh
```

#### 4. Test failure message

```bash
echo "This should fail" && false
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
