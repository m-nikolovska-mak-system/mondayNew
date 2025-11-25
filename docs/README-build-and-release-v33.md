# 📝 Build & Release Java App version 3 Workflow

## Overview

**Workflow Name:** `Build & Release Java App version 3`

## Triggers


## Jobs

### `build_jar`

### `detect_iss`

### `validate_inputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Check jar_cache_key**
   - Runs: `if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; th...`

### `build_installer`

### `upload_release`

### `notify_success`

### `notify_failure`

---

*This documentation is auto-generated. Do not edit manually.*
