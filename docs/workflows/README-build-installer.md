# 📝 Build Installer

**Generated:** 2025-11-25 14:14:13 UTC

---

## Overview

**Workflow File:** `.github/workflows/build-installer.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `build-installer`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `installer_file`: `${{ steps.set-installer-path.outputs.installer_file }}`

**Steps:**

1. **Checkout repo**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `ref`: `${{ inputs.release_tag }}`

2. **Restore cached JAR**
   - 📦 Action: `actions/cache/restore@v3`
   - ⚙️ Config:
     - `path`: `build/libs/*.jar`
     - `key`: `${{ inputs.jar_cache_key }}`

3. **Check JAR presence**
   - 💻 Run: `if (!(Test-Path "build\libs\*.jar")) {   Write-Error "JAR file not found after cache restore."   exit 1 }...`

4. **Get JAR filename**
   - 💻 Run: `$jar = Get-ChildItem "build\libs" -Filter *.jar -ErrorAction Stop | Select-Object -First 1 if (!$jar) {   Write-Error "N...`

5. **Install Inno Setup**
   - 💻 Run: `choco install innosetup --no-progress -y...`

6. **Validate Inno Setup install**
   - 💻 Run: `if (!(Test-Path "C:\Program Files (x86)\Inno Setup 6\ISCC.exe")) {   Write-Error "Inno Setup not installed correctly."  ...`

7. **Build setup.exe with Inno Setup**
   - 💻 Run: `Set-StrictMode -Version Latest $ErrorActionPreference = "Stop"  echo "=== Preparing Inno Setup build ==="  # Find ISCC d...`

8. **Debug - Check what was created**
   - 💻 Run: `echo "=== Contents of output directory ===" if (Test-Path "output") {   Get-ChildItem output -Force } else {   echo "❌ O...`

9. **Set output installer path**
   - 💻 Run: `$installer = Get-ChildItem "output" -Filter *.exe | Select-Object -First 1 if (-not $installer) {   Write-Error "❌ No in...`

10. **Upload installer artifact**
   - 📦 Action: `actions/upload-artifact@v4`
   - ⚙️ Config:
     - `name`: `setup-installer`
     - `path`: `output/*.exe`

11. **Installer Build Complete**
   - 💻 Run: `echo "✅ Installer successfully built and uploaded."...`

---

*This documentation is auto-generated. Do not edit manually.*
