<div align="center">

# 🚀 Build & Release Java App

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/build-and-release.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build_jar`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
jar_path: ${{ steps.build.outputs.jar_path }}
jar_cache_key: ${{ steps.build.outputs.jar_cache_key }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
```

#### 2. Build JAR

```yaml
uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-jar.yml@main
with:
  release_tag: ${{ github.event.release.tag_name || 'dev' }}
  gradle_task: ${{ env.GRADLE_TASK }}
  java_version: ${{ env.JAVA_VERSION }}
  java_distribution: ${{ env.JAVA_DISTRIBUTION }}
```

</details>

### 🎯 `detect_iss`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
setup_script: ${{ steps.detect.outputs.setup_script }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
```

#### 2. Detect ISS setup script

```yaml
uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/detect-setup-script.yml@main
with:
  pattern: **/*.iss
  fail_if_missing: True
```

</details>

### 🎯 `validate_inputs`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Validate JAR cache key

```bash
if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; then
  echo "::error::JAR cache key is empty - build may have failed"
  exit 1
fi
echo "✓ JAR cache key validated: ${{ needs.build_jar.outputs.jar_cache_key }}"
```

#### 2. Validate JAR path

```bash
if [ -z "${{ needs.build_jar.outputs.jar_path }}" ]; then
  echo "::error::JAR path is empty - artifact may not have been created"
  exit 1
fi
echo "✓ JAR path validated: ${{ needs.build_jar.outputs.jar_path }}"
```

</details>

### 🎯 `build_installer`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
installer_artifact_name: ${{ steps.installer.outputs.installer_artifact_name }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
```

#### 2. Build installer

```yaml
uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main
with:
  setup_script: ${{ needs.detect_iss.outputs.setup_script }}
  jar_path: ${{ needs.build_jar.outputs.jar_path }}
  jar_cache_key: ${{ needs.build_jar.outputs.jar_cache_key }}
  app_name: ${{ github.event.repository.name }}
  app_version: ${{ github.event.release.tag_name || 'dev' }}
```

</details>

### 🎯 `upload_release`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
```

#### 2. Upload to release

```yaml
uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/upload-release.yml@main
with:
  tag_name: ${{ github.event.release.tag_name }}
  artifact_name: ${{ needs.build_installer.outputs.installer_artifact_name }}
```

</details>

### 🎯 `notify_success`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main`

### 🎯 `notify_failure`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main`

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
