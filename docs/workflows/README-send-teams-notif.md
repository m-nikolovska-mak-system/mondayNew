# 📝 Send Teams Notification

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/send-teams-notif.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `notify`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Send Microsoft Teams notification**
   - 💻 Run: `set -e  # Validate webhook URL if [ -z "$TEAMS_WEBHOOK_URL" ]; then   echo "❌ Missing teams_webhook_url secret."   exit ...`

---

*This documentation is auto-generated. Do not edit manually.*
