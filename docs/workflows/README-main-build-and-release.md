# 📝 Main Build and Release

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/main-build-and-release.yml`

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

### `build_installer`

**Runner:** `unknown`

**Steps:**

### `upload_release`

**Runner:** `unknown`

**Steps:**

### `notify-on-failure`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Report failure**
   - 💻 Run: `echo "❌ Workflow failed" echo "Failed jobs: ${{ toJSON(needs) }}"...`

---

*This documentation is auto-generated. Do not edit manually.*
