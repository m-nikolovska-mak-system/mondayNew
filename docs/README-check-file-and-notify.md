<div align="center">

# 🚀 Detect File Changes + Notify Teams

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/check-file-and-notify.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check_changes`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/3check-file-changes.yml@main`

### 🎯 `debug_print`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Step 1

```bash
echo "changed files:  ${{ needs.check_changes.outputs.changed_files_list }}"
echo "all changed:    ${{ needs.check_changes.outputs.all_changed_files }}"
```

</details>

### 🎯 `notify_if_changed`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main`

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
