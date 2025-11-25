# 📝 Branch Name Check

**Generated:** 2025-11-25 14:32:46 UTC

---

## Overview

**Workflow File:** `.github/workflows/branch-check.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check-branch`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - 📦 Action: `actions/checkout@v4`

2. **Get branch name**
   - 💻 Run: `# Try multiple methods to get branch name if [ -n "$GITHUB_HEAD_REF" ]; then   # PR event   branch="$GITHUB_HEAD_REF"   ...`

3. **Check branch naming convention**
   - 💻 Run: `branch="${{ steps.branch.outputs.branch }}" echo "" echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" echo "🔍 Branch Name Valida...`

4. **Additional branch checks**
   - 💻 Run: `branch="${{ steps.branch.outputs.branch }}"  echo "" echo "🔍 Additional Checks:" echo ""  # Check for spaces if [[ "$bra...`

---

*This documentation is auto-generated. Do not edit manually.*
