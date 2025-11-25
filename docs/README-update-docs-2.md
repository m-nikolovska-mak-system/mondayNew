<div align="center">

# 🚀 Update Docs for Workflows

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/update-docs-2.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `update-docs`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Step 1

```yaml
uses: actions/checkout@v4
```

#### 2. Generate docs for main action

```yaml
uses: tj-actions/auto-doc@v3
with:
  filename: action.yml
  output: README.md
```

#### 3. Generate docs for reusable workflow

```yaml
uses: tj-actions/auto-doc@v3
with:
  filename: .github/workflows/notify-app-changes-v3.yml
  output: docs/reusable.md
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
