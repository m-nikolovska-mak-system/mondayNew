# 📝 Build Windows Installer Workflow

## Overview

**Workflow Name:** `Build Windows Installer`

## Triggers


## Jobs

### `build-installer`

**Runner:** `windows-latest`

**Steps:**

1. **Checkout repo**
   - Uses: `actions/checkout@v4`
2. **Download built JAR from previous workflow**
   - Uses: `actions/download-artifact@v4`
3. **Verify JAR**
   - Runs: `dir build\libs...`
4. **Install Inno Setup**
   - Runs: `choco install innosetup --no-progress -y...`
5. **Build setup.exe**
   - Runs: `"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" .github\setup...`
6. **Upload setup.exe as artifact**
   - Uses: `actions/upload-artifact@v4`
7. **Check output folder**
   - Runs: `dir output...`
8. **Upload setup.exe to GitHub Release**
   - Uses: `softprops/action-gh-release@v2`

---

*This documentation is auto-generated. Do not edit manually.*
