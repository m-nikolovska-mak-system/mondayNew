# 📝 Branch Name Validation Workflow

## Overview

**Workflow Name:** `Branch Name Validation`

## Triggers


## Jobs

### `branch-naming-rules`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v3`
2. **Validate branch name on create**
   - Runs: `BRANCH_NAME="${GITHUB_REF#refs/heads/}"...`
3. **Validate branch name on push**
   - Uses: `deepakputhraya/action-branch-name@master`
4. **Extract Jira Ticket Key**
   - Runs: `BRANCH_NAME="${GITHUB_REF#refs/heads/}"...`
5. **Validate Jira Ticket Exists**
   - Runs: `echo "Checking Jira ticket: ${{ steps.extract.outputs.ticket...`
6. **Notify Microsoft Teams on failure**
   - Runs: `curl -H 'Content-Type: application/json' \...`
7. **Create GitHub Issue on violation**
   - Runs: `BRANCH_NAME="${GITHUB_REF#refs/heads/}"...`
8. **Comment on PR if branch name is invalid**
   - Uses: `marocchino/sticky-pull-request-comment@v2`

---

*This documentation is auto-generated. Do not edit manually.*
