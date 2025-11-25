<div align="center">

# 🚀 Main Build and Release

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/main-build-and-release.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build_jar`

**📞 Calls:** `./.github/workflows/build-jar.yml`

### 🎯 `detect_iss`

**📞 Calls:** `./.github/workflows/detect-setup-script.yml`

### 🎯 `build_installer`

**📞 Calls:** `./.github/workflows/build-installer.yml`

### 🎯 `upload_release`

**📞 Calls:** `./.github/workflows/upload-release.yml`

### 🎯 `notify-on-failure`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Report failure

```bash
echo "❌ Workflow failed"
echo "Failed jobs: ${{ toJSON(needs) }}"
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
