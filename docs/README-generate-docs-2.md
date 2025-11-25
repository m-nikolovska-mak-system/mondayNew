<div align="center">

# 🚀 Generate Docs

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/generate-docs-2.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `generate-docs`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repository

```yaml
uses: actions/checkout@v4
```

#### 2. Set up Python

```yaml
uses: actions/setup-python@v5
with:
  python-version: 3.11
```

#### 3. Install dependencies

```bash
pip install pyyaml
```

#### 4. Run documentation generator

```bash
python scripts/generate_docs.py
```

#### 5. Commit and push changes

```bash
git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"
git add README.md docs/workflows.md
git commit -m "Update docs [skip ci]" || echo "No changes to commit"
git push
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
