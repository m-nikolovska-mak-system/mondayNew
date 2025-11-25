<div align="center">

# 🚀 Check File Changes

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/check-file-changes.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
changed: ${{ steps.detect.outputs.changed }}
files: ${{ steps.detect.outputs.files }}
current_ref: ${{ steps.refs.outputs.current }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repository

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 0
```

#### 2. Resolve refs

```bash
current="${{ inputs.current_ref }}"
previous="${{ inputs.previous_ref }}"

# Auto-detect current ref
if [ -z "$current" ]; then
# ... (truncated)
```

#### 3. Detect changes

```bash
pattern="${{ inputs.file_pattern }}"
prev="${{ steps.refs.outputs.previous }}"
curr="${{ steps.refs.outputs.current }}"

echo "🔍 Searching for pattern: $pattern"
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
