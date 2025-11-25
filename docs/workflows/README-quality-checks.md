# 📝 Simple Quality Checks

**Generated:** 2025-11-25 14:32:46 UTC

---

## Overview

**Workflow File:** `.github/workflows/quality-checks.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `quality-checks`

**Runner:** `ubuntu-latest`

**Steps:**

1. **📥 Checkout code**
   - 📦 Action: `actions/checkout@v4`

2. **✅ Check README exists**
   - 💻 Run: `echo "🔍 Checking if README.md exists..." if [ -f README.md ]; then   echo "✅ README.md found"   echo "status=pass" >> $G...`

3. **📄 Check README has content**
   - 💻 Run: `echo "🔍 Checking README.md has content..." if [ ! -f README.md ]; then   echo "⚠️  Skipping (README doesn't exist)"   ec...`

4. **🐚 Check shell scripts**
   - 💻 Run: `echo "🔍 Looking for shell scripts..." shfiles=$(find . -name "*.sh" -type f 2>/dev/null | wc -l)  if [ "$shfiles" -eq 0 ...`

5. **📝 Check Markdown files**
   - 💻 Run: `echo "🔍 Installing markdownlint..." npm install -g markdownlint-cli >/dev/null 2>&1  echo "🔍 Checking Markdown files..."...`

6. **📊 Summary Report**
   - 💻 Run: `echo "" echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" echo "📊 QUALITY CHECKS SUMMARY" echo "━━━━━━━━━━━━━━━━━━━━━━...`

---

*This documentation is auto-generated. Do not edit manually.*
