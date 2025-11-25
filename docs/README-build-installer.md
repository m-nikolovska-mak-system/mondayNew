# 📝 Build Installer Workflow

## Overview

**Workflow Name:** `Build Installer`

## Triggers


## Jobs

### `build-installer`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repo**
   - Uses: `actions/checkout@v4`
2. **Restore cached JAR**
   - Uses: `actions/cache/restore@v3`
3. **Check JAR presence**
   - Runs: `if (!(Test-Path "build\libs\*.jar")) {...`
4. **Get JAR filename**
   - Runs: `$jar = Get-ChildItem "build\libs" -Filter *.jar -ErrorAction...`
5. **Install Inno Setup**
   - Runs: `choco install innosetup --no-progress -y...`
6. **Validate Inno Setup install**
   - Runs: `if (!(Test-Path "C:\Program Files (x86)\Inno Setup 6\ISCC.ex...`
7. **Build setup.exe with Inno Setup**
   - Runs: `Set-StrictMode -Version Latest...`
8. **Debug - Check what was created**
   - Runs: `echo "=== Contents of output directory ==="...`
9. **Set output installer path**
   - Runs: `$installer = Get-ChildItem "output" -Filter *.exe | Select-O...`
10. **Upload installer artifact**
   - Uses: `actions/upload-artifact@v4`
11. **Installer Build Complete**
   - Runs: `echo "✅ Installer successfully built and uploaded."...`

---

*This documentation is auto-generated. Do not edit manually.*
