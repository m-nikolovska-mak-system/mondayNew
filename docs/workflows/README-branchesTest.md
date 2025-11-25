# 📝 Branch naming

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/branchesTest.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `branch-naming-rules`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v3`

2. **Validate branch name on create**
   - 💻 Run: `BRANCH_NAME="${GITHUB_REF#refs/heads/}" echo "Checking branch name: $BRANCH_NAME" if [[ ! "$BRANCH_NAME" =~ ^(hot-fix-)?...`

3. **Validate branch name on push**
   - 📦 Action: `deepakputhraya/action-branch-name@master`
   - ⚙️ Config:
     - `regex`: `.*`
     - `min_length`: `10`
     - `max_length`: `100`

4. **Debug extracted ticket**
   - 💻 Run: `BRANCH_NAME="${GITHUB_REF#refs/heads/}" TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[0-9]+' | tail -n1) echo "Bra...`

5. **Debug Jira API call**
   - 💻 Run: `BRANCH_NAME="${GITHUB_REF#refs/heads/}" TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[0-9]+' | tail -n1) echo "Che...`

6. **Extract Jira Ticket Key**
   - 💻 Run: `BRANCH_NAME="${GITHUB_REF#refs/heads/}" echo "Branch: $BRANCH_NAME" TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[...`

7. **Validate Jira Ticket Exists**
   - 💻 Run: `echo "Checking Jira ticket: ${{ steps.extract.outputs.ticket }}" RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \   -...`

8. **Comment on PR if branch name is invalid**
   - 📦 Action: `marocchino/sticky-pull-request-comment@v2`
   - ⚙️ Config:
     - `message`: `⚠️ **Branch name does not follow the convention!**
Please rename your branch to match one of the following formats:
- `hot-fix/ABC-login-ERP-12345`
- `ABC-login-ERP-12345`
`

---

*This documentation is auto-generated. Do not edit manually.*
