<div align="center">

# 🚀 Notify App Changes on Release

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/release-reminder.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `check_app_change`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
should_notify: ${{ steps.check.outputs.should_notify }}
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

#### 2. Get current release tag

```bash
echo "tag=${{ github.event.release.tag_name }}" >> $GITHUB_OUTPUT
```

#### 3. Get previous tag

```bash
prev_tag=$(git tag --sort=-creatordate | grep -B1 "${{ steps.current_tag.outputs.tag }}" | head -n1)
echo "prev_tag=$prev_tag" >> $GITHUB_OUTPUT
```

#### 4. Check if App.java changed

```bash
if git diff --name-only ${{ steps.previous_tag.outputs.prev_tag }} ${{ steps.current_tag.outputs.tag }} | grep -q 'oneProjectWed/src/java/com/miha/app/App.java'; then
  echo "should_notify=true" >> $GITHUB_OUTPUT
else
  echo "should_notify=false" >> $GITHUB_OUTPUT
fi
```

</details>

### 🎯 `notify`

**📞 Calls:** `./.github/workflows/teams-notif-simple.yml`

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
