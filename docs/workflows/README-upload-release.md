# 📝 Upload Release Artifact

**Generated:** 2025-11-25 14:14:13 UTC

---

## Overview

**Workflow File:** `.github/workflows/upload-release.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `upload`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Download installer artifact**
   - 📦 Action: `actions/download-artifact@v4`
   - ⚙️ Config:
     - `name`: `setup-installer`
     - `path`: `./release-assets`

2. **Verify artifact exists**
   - 💻 Run: `echo "=== Files in release-assets ===" ls -lh ./release-assets/  files=$(ls ./release-assets/*.exe 2>/dev/null) if [ -z ...`

3. **Upload to GitHub Release**
   - 📦 Action: `softprops/action-gh-release@v2`
   - ⚙️ Config:
     - `files`: `./release-assets/*.exe`
     - `tag_name`: `${{ inputs.tag_name }}`

---

*This documentation is auto-generated. Do not edit manually.*
