<div align="center">

# 🚀 Upload Release Artifact

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/upload-release.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `upload`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Download installer artifact

```yaml
uses: actions/download-artifact@v4
with:
  name: setup-installer
  path: ./release-assets
```

#### 2. Verify artifact exists

```bash
echo "=== Files in release-assets ==="
ls -lh ./release-assets/

files=$(ls ./release-assets/*.exe 2>/dev/null)
if [ -z "$files" ]; then
# ... (truncated)
```

#### 3. Upload to GitHub Release

```yaml
uses: softprops/action-gh-release@v2
with:
  files: ./release-assets/*.exe
  tag_name: ${{ inputs.tag_name }}
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
