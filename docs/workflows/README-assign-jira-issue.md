# 📝 Assign Jira Issue

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/assign-jira-issue.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `assign`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Install jq and python3**
   - 💻 Run: `sudo apt-get update -y sudo apt-get install -y jq python3...`

2. **Assign issue in Jira**
   - 💻 Run: `set -e if [ -z "$JIRA_EMAIL" ] || [ -z "$JIRA_API_TOKEN" ] || [ -z "$JIRA_URL" ]; then   echo "Missing Jira secrets: JIR...`

---

*This documentation is auto-generated. Do not edit manually.*
