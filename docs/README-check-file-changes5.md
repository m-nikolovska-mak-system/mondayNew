<div align="center">

# 🚀 🧩 Detect & Act on File Changes

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/check-file-changes5.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check_changes`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/check-file-changes.yml@main`

### 🎯 `run_on_change`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. ✅ Files changed

```bash
echo "Changed files:"
echo "${{ needs.check_changes.outputs.changed_files_list }}"
# Add your logic below (tests, build, deploy, etc.)
```

</details>

### 🎯 `run_on_no_change`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. ℹ️ No watched files changed

```bash
echo "No relevant files changed. Skipping build."
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
