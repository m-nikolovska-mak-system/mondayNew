<div align="center">

# 🚀 Notify on App.java Changes

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/notify-app-changes-v3.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check-file-changes`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/check-for-file-changes.yml@main`

### 🎯 `debug-outputs`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Print check results

```bash
echo "Job status: ${{ needs.check-file-changes.result }}"
echo "Files changed: ${{ needs.check-file-changes.outputs.files_changed }}"
echo "Changed files list: ${{ needs.check-file-changes.outputs.changed_files_list }}"
```

</details>

### 🎯 `send-teams-notification`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/send-teams-notification-v2.yml@main`

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
