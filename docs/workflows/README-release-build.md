# 📝 Build and Release

**Generated:** 2025-11-26 12:27:54 UTC

---

## Overview

**Workflow File:** `.github/workflows/release-build.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `build-jar`

**Runner:** `unknown`

**Steps:**

### `detect-setup-script`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `setup_script`: `${{ steps.detect.outputs.script }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `ref`: `${{ github.event.inputs.release_tag || github.event.release.tag_name || 'main' }}`

2. **Find .iss script**
   - 💻 Run: `echo "🔍 Looking for Inno Setup script..."  # Look for .iss files in root and common directories script=$(find . -maxdept...`

### `build-installer`

**Runner:** `unknown`

**Steps:**

### `upload-to-release`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Download installer artifact**
   - 📦 Action: `actions/download-artifact@v4`
   - ⚙️ Config:
     - `name`: `${{ needs.build-installer.outputs.installer_artifact_name }}`
     - `path`: `./installer`

2. **Verify installer exists**
   - 💻 Run: `echo "📦 Downloaded artifacts:" ls -lh installer/ echo ""  # Check if any .exe files exist if ! ls installer/*.exe 1> /de...`

3. **Upload installer to GitHub Release**
   - 📦 Action: `softprops/action-gh-release@v2`
   - ⚙️ Config:
     - `files`: `installer/*.exe`
     - `tag_name`: `${{ github.event.release.tag_name }}`
     - `fail_on_unmatched_files`: `True`

4. **Success notification**
   - 💻 Run: `echo "✅ Installer successfully uploaded to release ${{ github.event.release.tag_name }}"`

### `test-summary`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Display test results**
   - 💻 Run: `echo "==========================================" echo "🧪 TEST MODE - BUILD SUMMARY" echo "=============================...`

---

*This documentation is auto-generated. Do not edit manually.*
