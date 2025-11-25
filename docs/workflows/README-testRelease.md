# 📝 Teams Notification Template THIS IS THE GOOD ONE

**Generated:** 2025-11-25 14:37:06 UTC

---

## Overview

**Workflow File:** `.github/workflows/testRelease.yml`

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
   - ⚙️ Config:
     - `fetch-depth`: `0`

2. **Detect changed files**
   - 💻 Run: `set -e echo "🔍 Detecting changed files..."  if [ "${{ github.event.before }}" = "000000000000000000000000000000000000000...`

3. **Send Microsoft Teams notification**
   - 💻 Run: `set -e  # Validate webhook URL if [ -z "$TEAMS_WEBHOOK_URL" ]; then   echo "❌ Missing teams_webhook_url secret."   exit ...`

---

*This documentation is auto-generated. Do not edit manually.*
