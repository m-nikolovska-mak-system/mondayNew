# 📝 Build & Release Java App Workflow

## Overview

**Workflow Name:** `Build & Release Java App`

## Triggers


## Jobs

### `build_jar`

### `detect_iss`

### `validate_inputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Validate JAR cache key**
   - Runs: `if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; th...`
2. **Validate JAR path**
   - Runs: `if [ -z "${{ needs.build_jar.outputs.jar_path }}" ]; then...`

### `build_installer`

### `upload_release`

### `notify_success`

### `notify_failure`

---

*This documentation is auto-generated. Do not edit manually.*
