# 📝 Send Teams Notification

**Generated:** 2025-11-25 14:06:40 UTC

---

## Overview

**Workflow File:** `.github/workflows/teams-notif-simple.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `notify-teams`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Send Microsoft Teams notification**
   - 💻 Run: `set -e  if [ -z "$TEAMS_WEBHOOK_URL" ]; then   echo "❌ Missing teams_webhook_url secret."   exit 1 fi  ACTOR="${{ github...`

---

*This documentation is auto-generated. Do not edit manually.*
