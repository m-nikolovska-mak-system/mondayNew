<div align="center">

# 🚀 Build Installer

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/build-installer.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build-installer`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
installer_file: ${{ steps.set-installer-path.outputs.installer_file }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repo

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ inputs.release_tag }}
```

#### 2. Restore cached JAR

```yaml
uses: actions/cache/restore@v3
with:
  path: build/libs/*.jar
  key: ${{ inputs.jar_cache_key }}
```

#### 3. Check JAR presence

```bash
if (!(Test-Path "build\libs\*.jar")) {
  Write-Error "JAR file not found after cache restore."
  exit 1
}
```

#### 4. Get JAR filename

```bash
$jar = Get-ChildItem "build\libs" -Filter *.jar -ErrorAction Stop | Select-Object -First 1
if (!$jar) {
  Write-Error "No JAR file found!"
  exit 1
}
# ... (truncated)
```

#### 5. Install Inno Setup

```bash
choco install innosetup --no-progress -y
```

#### 6. Validate Inno Setup install

```bash
if (!(Test-Path "C:\Program Files (x86)\Inno Setup 6\ISCC.exe")) {
  Write-Error "Inno Setup not installed correctly."
  exit 1
}
```

#### 7. Build setup.exe with Inno Setup

```bash
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

echo "=== Preparing Inno Setup build ==="

# ... (truncated)
```

#### 8. Debug - Check what was created

```bash
echo "=== Contents of output directory ==="
if (Test-Path "output") {
  Get-ChildItem output -Force
} else {
  echo "❌ Output directory does not exist!"
# ... (truncated)
```

#### 9. Set output installer path

```bash
$installer = Get-ChildItem "output" -Filter *.exe | Select-Object -First 1
if (-not $installer) {
  Write-Error "❌ No installer .exe found in output directory!"
  exit 1
}
# ... (truncated)
```

#### 10. Upload installer artifact

```yaml
uses: actions/upload-artifact@v4
with:
  name: setup-installer
  path: output/*.exe
```

#### 11. Installer Build Complete

```bash
echo "✅ Installer successfully built and uploaded."
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
