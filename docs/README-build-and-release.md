# 📝 Build & Release Java App Workflow

## Overview

**Workflow Name:** `Build & Release Java App`

## Triggers


## Jobs

### `build_jar`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Build JAR**
   - Uses: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-jar.yml@main`

### `detect_iss`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Detect ISS setup script**
   - Uses: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/detect-setup-script.yml@main`

### `validate_inputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Validate JAR cache key**
   - Runs: `if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; th...`
2. **Validate JAR path**
   - Runs: `if [ -z "${{ needs.build_jar.outputs.jar_path }}" ]; then...`

### `build_installer`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Build installer**
   - Uses: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main`

### `upload_release`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Upload to release**
   - Uses: `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/upload-release.yml@main`

### `notify_success`

### `notify_failure`

---

*This documentation is auto-generated. Do not edit manually.*
