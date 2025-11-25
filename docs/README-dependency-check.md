<div align="center">

# 🚀 Dependency Health

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/dependency-check.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check-deps`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Step 1

```yaml
uses: actions/checkout@v4
```

#### 2. Check package.json exists

```bash
if [ -f package.json ]; then
  echo "✅ package.json found"
  cat package.json | jq '.dependencies // {}, .devDependencies // {}' || true
else
  echo "ℹ️  No package.json - skipping"
# ... (truncated)
```

#### 3. Check for package-lock.json

```bash
if [ -f package-lock.json ]; then
  echo "✅ package-lock.json present"
else
  echo "⚠️  No package-lock.json - dependencies not locked"
fi
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
