<div align="center">

# 🚀 🧪 Test File Change Detection

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/test-check-file-changes.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check_changes`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/check-for-file-changes.yml@main`

### 🎯 `on_changes`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. ✅ Watched files changed

```bash
echo "Changed files:"
echo "${{ needs.check_changes.outputs.changed_files_list }}"
```

</details>

### 🎯 `on_no_changes`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. ℹ️ No relevant changes

```bash
echo "No watched files changed!"
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
