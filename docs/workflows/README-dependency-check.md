# 📝 Dependency Health

**Generated:** 2025-11-26 12:27:54 UTC

---

## Overview

**Workflow File:** `.github/workflows/dependency-check.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check-deps`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - 📦 Action: `actions/checkout@v4`

2. **Check package.json exists**
   - 💻 Run: `if [ -f package.json ]; then   echo "✅ package.json found"   cat package.json | jq '.dependencies // {}, .devDependencie...`

3. **Check for package-lock.json**
   - 💻 Run: `if [ -f package-lock.json ]; then   echo "✅ package-lock.json present" else   echo "⚠️  No package-lock.json - dependenc...`

---

*This documentation is auto-generated. Do not edit manually.*
