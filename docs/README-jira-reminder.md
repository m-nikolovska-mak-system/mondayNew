# 📝 Create Jira Task on Release Workflow

## Overview

**Workflow Name:** `Create Jira Task on Release`

## Triggers


## Jobs

### `create-jira-task`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - Uses: `actions/checkout@v4`
2. **Create Jira task**
   - Uses: `atlassian/gajira-create@v3`

---

*This documentation is auto-generated. Do not edit manually.*
