<div align="center">

# 🚀 Simple Quality Checks

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/quality-checks.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `quality-checks`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. 📥 Checkout code

```yaml
uses: actions/checkout@v4
```

#### 2. ✅ Check README exists

```bash
echo "🔍 Checking if README.md exists..."
if [ -f README.md ]; then
  echo "✅ README.md found"
  echo "status=pass" >> $GITHUB_OUTPUT
else
# ... (truncated)
```

#### 3. 📄 Check README has content

```bash
echo "🔍 Checking README.md has content..."
if [ ! -f README.md ]; then
  echo "⚠️  Skipping (README doesn't exist)"
  echo "status=skip" >> $GITHUB_OUTPUT
  exit 0
# ... (truncated)
```

#### 4. 🐚 Check shell scripts

```bash
echo "🔍 Looking for shell scripts..."
shfiles=$(find . -name "*.sh" -type f 2>/dev/null | wc -l)

if [ "$shfiles" -eq 0 ]; then
  echo "ℹ️  No shell scripts found - skipping"
# ... (truncated)
```

#### 5. 📝 Check Markdown files

```bash
echo "🔍 Installing markdownlint..."
npm install -g markdownlint-cli >/dev/null 2>&1

echo "🔍 Checking Markdown files..."
if markdownlint '**/*.md' --ignore node_modules 2>&1; then
# ... (truncated)
```

#### 6. 📊 Summary Report

```bash
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 QUALITY CHECKS SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
