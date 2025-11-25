<div align="center">

# 🚀 Test File Change Detection

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/test-file-detection.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `test-detection`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/3check-file-changes.yml@main`

### 🎯 `show-results`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Show what was detected

```bash
echo "=========================================="
echo "🧪 FILE DETECTION TEST RESULTS"
echo "=========================================="
echo ""
echo "📊 Comparison: ${{ needs.test-detection.outputs.comparison_info }}"
# ... (truncated)
```

#### 2. Create test summary

```bash
echo "# 🧪 File Detection Test Results" >> $GITHUB_STEP_SUMMARY
echo "" >> $GITHUB_STEP_SUMMARY
echo "## Comparison" >> $GITHUB_STEP_SUMMARY
echo "\`${{ needs.test-detection.outputs.comparison_info }}\`" >> $GITHUB_STEP_SUMMARY
echo "" >> $GITHUB_STEP_SUMMARY
# ... (truncated)
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
