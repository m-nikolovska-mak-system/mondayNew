# 📝 Branch Name Validation

**Generated:** 2025-11-25 14:32:46 UTC

---

## Overview

**Workflow File:** `.github/workflows/branchNamingTwo.yml`

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
     - `regex`: `^(hot-fix-)?[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*-ERP-[0-9]+$`
     - `min_length`: `10`
     - `max_length`: `100`

4. **Extract Jira Ticket Key**
   - 💻 Run: `BRANCH_NAME="${GITHUB_REF#refs/heads/}" echo "Branch: $BRANCH_NAME" TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[...`

5. **Validate Jira Ticket Exists**
   - 💻 Run: `echo "Checking Jira ticket: ${{ steps.extract.outputs.ticket }}" RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \   -...`

6. **Notify Microsoft Teams on failure**
   - 💻 Run: `curl -H 'Content-Type: application/json' \ -d ' {   "@type": "MessageCard",   "@context": "https://schema.org/extensions...`

7. **Create GitHub Issue on violation**
   - 💻 Run: `BRANCH_NAME="${GITHUB_REF#refs/heads/}" gh issue create \   --title "Branch Naming Violation: $BRANCH_NAME" \   --body "...`

8. **Comment on PR if branch name is invalid**
   - 📦 Action: `marocchino/sticky-pull-request-comment@v2`
   - ⚙️ Config:
     - `message`: `⚠️ **Branch name does not follow the convention or Jira ticket is invalid!**
Please rename your branch to match one of the following formats:
- `hot-fix/ABC-login-ERP-12345`
- `ABC-login-ERP-12345`
`

---

*This documentation is auto-generated. Do not edit manually.*
