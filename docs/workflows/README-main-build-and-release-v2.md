# 📝 Build & Release Java App

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/main-build-and-release-v2.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `build_jar`

**Runner:** `unknown`

**Steps:**

### `detect_iss`

**Runner:** `unknown`

**Steps:**

### `validate_inputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Check jar_cache_key**
   - 💻 Run: `if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; then   echo "::error::JAR cache key is empty!"   exit 1 fi...`

### `build_installer`

**Runner:** `unknown`

**Steps:**

### `upload_release`

**Runner:** `unknown`

**Steps:**

### `notify_failure`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
