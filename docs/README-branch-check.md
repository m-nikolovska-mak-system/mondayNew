<div align="center">

# 🚀 Branch Name Check

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/branch-check.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check-branch`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Step 1

```yaml
uses: actions/checkout@v4
```

#### 2. Get branch name

```bash
# Try multiple methods to get branch name
if [ -n "$GITHUB_HEAD_REF" ]; then
  # PR event
  branch="$GITHUB_HEAD_REF"
  echo "📍 Branch from PR: $branch"
# ... (truncated)
```

#### 3. Check branch naming convention

```bash
branch="${{ steps.branch.outputs.branch }}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 Branch Name Validation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
# ... (truncated)
```

#### 4. Additional branch checks

```bash
branch="${{ steps.branch.outputs.branch }}"

echo ""
echo "🔍 Additional Checks:"
echo ""
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
