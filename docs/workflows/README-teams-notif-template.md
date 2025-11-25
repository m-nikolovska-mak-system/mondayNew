# 📝 Teams Notification Template

**Generated:** 2025-11-25 14:14:13 UTC

---

## Overview

**Workflow File:** `.github/workflows/teams-notif-template.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `send-notification`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - 📦 Action: `actions/checkout@v4`

2. **Make script executable**
   - 💻 Run: `chmod +x ./scripts/send-teams-notification.sh...`

3. **Send Microsoft Teams notification**
   - 💻 Run: `./scripts/send-teams-notification.sh...`

4. **Test failure message**
   - 💻 Run: `echo "This should fail" && false...`

---

*This documentation is auto-generated. Do not edit manually.*
