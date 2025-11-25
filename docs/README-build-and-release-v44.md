<div align="center">

# 🚀 Build & Release Java App (version 3)

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/build-and-release-v44.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build_jar`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-jar.yml@main`

### 🎯 `detect_iss`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/detect-setup-script.yml@main`

### 🎯 `validate_inputs`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Validate jar_cache_key

```bash
if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; then
  echo "::error::JAR cache key is empty!"
  exit 1
fi
```

</details>

### 🎯 `build_installer`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main`

### 🎯 `upload_release`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/upload-release.yml@main`

### 🎯 `notify_success`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main`

### 🎯 `notify_failure`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main`

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
