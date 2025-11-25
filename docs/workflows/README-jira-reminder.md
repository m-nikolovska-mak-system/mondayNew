# 📝 Create Jira Task on Release

**Generated:** 2025-11-25 14:45:12 UTC

---

## Overview

**Workflow File:** `.github/workflows/jira-reminder.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `create-jira-task`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - 📦 Action: `actions/checkout@v4`

2. **Create Jira task**
   - 📦 Action: `atlassian/gajira-create@v3`
   - ⚙️ Config:
     - `project`: `DEMO`
     - `issuetype`: `Task`
     - `summary`: `Prepare new installer for App.java changes`
     - `description`: `App.java was modified in the latest release.
Please review and rebuild the installer if necessary.
`
     - `assignee`: `mihaela.nikolovska@students.finki.ukim.mk`

---

*This documentation is auto-generated. Do not edit manually.*
