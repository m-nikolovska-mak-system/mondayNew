<div align="center">

# 🚀 Generate workflow docs

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/generate-docs.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build-doc`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repo

```yaml
uses: actions/checkout@v4
```

#### 2. Generate README with auto-doc

```yaml
uses: tj-actions/auto-doc@v3
with:
  file: ${{ github.event.inputs.filename }}
  output: ${{ github.event.inputs.output }}
```

#### 3. Commit generated docs

```yaml
uses: EndBug/add-and-commit@v9
with:
  author_name: github-actions[bot]
  author_email: 41898282+github-actions[bot]@users.noreply.github.com
  message: chore(docs): update workflow docs for ${{ github.event.input...
  add: ${{ github.event.inputs.output }}
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
