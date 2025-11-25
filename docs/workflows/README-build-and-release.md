# 📝 Build & Release Java App

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/build-and-release.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `build_jar`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `jar_path`: `${{ steps.build.outputs.jar_path }}`
- `jar_cache_key`: `${{ steps.build.outputs.jar_cache_key }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`

2. **Build JAR**
   - 📦 Action: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-jar.yml@main`
   - ⚙️ Config:
     - `release_tag`: `${{ github.event.release.tag_name || 'dev' }}`
     - `gradle_task`: `${{ env.GRADLE_TASK }}`
     - `java_version`: `${{ env.JAVA_VERSION }}`
     - `java_distribution`: `${{ env.JAVA_DISTRIBUTION }}`

### `detect_iss`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `setup_script`: `${{ steps.detect.outputs.setup_script }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`

2. **Detect ISS setup script**
   - 📦 Action: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/detect-setup-script.yml@main`
   - ⚙️ Config:
     - `pattern`: `**/*.iss`
     - `fail_if_missing`: `True`

### `validate_inputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Validate JAR cache key**
   - 💻 Run: `if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; then   echo "::error::JAR cache key is empty - build may have ...`

2. **Validate JAR path**
   - 💻 Run: `if [ -z "${{ needs.build_jar.outputs.jar_path }}" ]; then   echo "::error::JAR path is empty - artifact may not have bee...`

### `build_installer`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `installer_artifact_name`: `${{ steps.installer.outputs.installer_artifact_name }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`

2. **Build installer**
   - 📦 Action: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main`
   - ⚙️ Config:
     - `setup_script`: `${{ needs.detect_iss.outputs.setup_script }}`
     - `jar_path`: `${{ needs.build_jar.outputs.jar_path }}`
     - `jar_cache_key`: `${{ needs.build_jar.outputs.jar_cache_key }}`
     - `app_name`: `${{ github.event.repository.name }}`
     - `app_version`: `${{ github.event.release.tag_name || 'dev' }}`
     - `output_name`: `Setup-${{ github.event.release.tag_name || 'dev' }}`

### `upload_release`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`

2. **Upload to release**
   - 📦 Action: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/upload-release.yml@main`
   - ⚙️ Config:
     - `tag_name`: `${{ github.event.release.tag_name }}`
     - `artifact_name`: `${{ needs.build_installer.outputs.installer_artifact_name }}`

### `notify_success`

**Runner:** `unknown`

**Steps:**

### `notify_failure`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
