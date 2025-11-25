<div align="center">

# 🚀 Notify Teams on Changes

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/test-team-notify54.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `detect-changes`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
changed_files: ${{ steps.changes.outputs.files }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 2
```

#### 2. Get changed files

```bash
# For push events, compare with previous commit
if [ "${{ github.event_name }}" = "push" ]; then
  FILES=$(git diff --name-only HEAD^ HEAD | tr '\n' ',' | sed 's/,$//')
else
  # For manual dispatch, just list some key files
# ... (truncated)
```

</details>

### 🎯 `notify-teams`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main`

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
