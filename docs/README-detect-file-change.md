<div align="center">

# 🚀 Detect File Change

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/detect-file-change.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `detect`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
found: ${{ steps.result.outputs.found }}
files: ${{ steps.result.outputs.files }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Step 1

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 0
```

#### 2. Detect changed files

```bash
set -e
AFTER="${{ github.event.release.tag_name }}"
WATCHED_PATH="${{ inputs.watched_path }}"

git fetch --tags --quiet
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
