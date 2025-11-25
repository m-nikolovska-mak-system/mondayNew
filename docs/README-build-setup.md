<div align="center">

# 🚀 Build Windows Installer

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/build-setup.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build-installer`

**🖥️ Runner:** `windows-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repo

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ github.event.inputs.release_tag }}
```

#### 2. Download built JAR from previous workflow

```yaml
uses: actions/download-artifact@v4
with:
  name: app-jar
  path: build/libs
```

#### 3. Verify JAR

```bash
dir build\libs
```

#### 4. Install Inno Setup

```bash
choco install innosetup --no-progress -y
```

#### 5. Build setup.exe

```bash
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" .github\setup-script.iss
```

#### 6. Upload setup.exe as artifact

```yaml
uses: actions/upload-artifact@v4
with:
  name: setup-installer
  path: output/OneProjectWed-Setup.exe
```

#### 7. Check output folder

```bash
dir output
```

#### 8. Upload setup.exe to GitHub Release

```yaml
uses: softprops/action-gh-release@v2
with:
  files: output/OneProjectWed-Setup.exe
  tag_name: ${{ github.event.inputs.release_tag }}
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
