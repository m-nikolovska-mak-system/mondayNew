# 📝 Teams Notification

**Generated:** 2025-11-25 14:32:46 UTC

---

## Overview

**Workflow File:** `.github/workflows/teams-notify.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `notify`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Send simple Teams message**
   - 💻 Run: `echo "📤 Sending notification to Teams..."  # Check if webhook is set if [ -z "${{ secrets.TEAMS_WEBHOOK_URL }}" ]; then ...`

---

*This documentation is auto-generated. Do not edit manually.*
