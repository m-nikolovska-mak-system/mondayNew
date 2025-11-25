<div align="center">

# 🚀 Branch naming

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/branchesTest.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `branch-naming-rules`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v3
```

#### 2. Validate branch name on create

```bash
BRANCH_NAME="${GITHUB_REF#refs/heads/}"
echo "Checking branch name: $BRANCH_NAME"
if [[ ! "$BRANCH_NAME" =~ ^(hot-fix-)?[A-Z]{3}-[a-zA-Z0-9]+-ERP-[0-9]{5}$ ]]; then
  echo "❌ Invalid branch name: $BRANCH_NAME"
  exit 1
# ... (truncated)
```

#### 3. Validate branch name on push

```yaml
uses: deepakputhraya/action-branch-name@master
with:
  regex: .*
  min_length: 10
  max_length: 100
```

#### 4. Debug extracted ticket

```bash
BRANCH_NAME="${GITHUB_REF#refs/heads/}"
TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[0-9]+' | tail -n1)
echo "Branch name: $BRANCH_NAME"
echo "Extracted ticket: $TICKET"
if [ -z "$TICKET" ]; then
# ... (truncated)
```

#### 5. Debug Jira API call

```bash
BRANCH_NAME="${GITHUB_REF#refs/heads/}"
TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[0-9]+' | tail -n1)
echo "Checking Jira ticket: $TICKET"

RESPONSE=$(curl -s -u "${{ secrets.JIRA_USER }}:${{ secrets.JIRA_API_TOKEN }}" \
# ... (truncated)
```

#### 6. Extract Jira Ticket Key

```bash
BRANCH_NAME="${GITHUB_REF#refs/heads/}"
echo "Branch: $BRANCH_NAME"
TICKET=$(echo "$BRANCH_NAME" | grep -oE '[A-Z0-9]+-[0-9]+' | tail -n1)
echo "Extracted ticket: $TICKET"
echo "ticket=$TICKET" >> $GITHUB_OUTPUT
```

#### 7. Validate Jira Ticket Exists

```bash
echo "Checking Jira ticket: ${{ steps.extract.outputs.ticket }}"
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" \
  -u "${{ secrets.JIRA_USER }}:${{ secrets.JIRA_API_TOKEN }}" \
  -X GET \
  -H "Accept: application/json" \
# ... (truncated)
```

#### 8. Comment on PR if branch name is invalid

```yaml
uses: marocchino/sticky-pull-request-comment@v2
with:
  message: ⚠️ **Branch name does not follow the convention!** Please re...
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
