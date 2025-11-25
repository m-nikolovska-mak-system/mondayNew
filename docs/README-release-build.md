# 📝 Build and Release Workflow

## Overview

**Workflow Name:** `Build and Release`

## Triggers


## Jobs

### `build-jar`

### `detect-setup-script`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Find .iss script**
   - Runs: `echo "🔍 Looking for Inno Setup script..."...`

### `build-installer`

### `upload-to-release`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Download installer artifact**
   - Uses: `actions/download-artifact@v4`
2. **Verify installer exists**
   - Runs: `echo "📦 Downloaded artifacts:"...`
3. **Upload installer to GitHub Release**
   - Uses: `softprops/action-gh-release@v2`
4. **Success notification**
   - Runs: `echo "✅ Installer successfully uploaded to release ${{ githu...`

### `test-summary`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Display test results**
   - Runs: `echo "=========================================="...`

---

*This documentation is auto-generated. Do not edit manually.*
