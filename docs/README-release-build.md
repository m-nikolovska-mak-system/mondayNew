<div align="center">

# 🚀 Build and Release

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/release-build.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build-jar`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-jar.yml@main`

### 🎯 `detect-setup-script`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
setup_script: ${{ steps.detect.outputs.script }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ github.event.inputs.release_tag || github.event.release....
```

#### 2. Find .iss script

```bash
echo "🔍 Looking for Inno Setup script..."

# Look for .iss files in root and common directories
script=$(find . -maxdepth 2 -name "*.iss" -type f | head -n 1)

# ... (truncated)
```

</details>

### 🎯 `build-installer`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main`

### 🎯 `upload-to-release`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Download installer artifact

```yaml
uses: actions/download-artifact@v4
with:
  name: ${{ needs.build-installer.outputs.installer_artifact_name }}
  path: ./installer
```

#### 2. Verify installer exists

```bash
echo "📦 Downloaded artifacts:"
ls -lh installer/
echo ""

# Check if any .exe files exist
# ... (truncated)
```

#### 3. Upload installer to GitHub Release

```yaml
uses: softprops/action-gh-release@v2
with:
  files: installer/*.exe
  tag_name: ${{ github.event.release.tag_name }}
  fail_on_unmatched_files: True
```

#### 4. Success notification

```bash
echo "✅ Installer successfully uploaded to release ${{ github.event.release.tag_name }}"
```

</details>

### 🎯 `test-summary`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Display test results

```bash
echo "=========================================="
echo "🧪 TEST MODE - BUILD SUMMARY"
echo "=========================================="
echo ""
echo "✅ JAR Build:"
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
