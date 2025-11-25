<div align="center">

# 🚀 Simple README Generator

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/generate-readme-simple.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `generate-readme`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout

```yaml
uses: actions/checkout@v4
with:
  token: ${{ secrets.GITHUB_TOKEN }}
```

#### 2. Select workflow file

```bash
echo "workflow_file=.github/workflows/build-installer.yml" >> $GITHUB_OUTPUT
echo "basename=build-installer" >> $GITHUB_OUTPUT
```

#### 3. Ensure docs folder exists

```bash
mkdir -p docs
```

#### 4. Prepare initial README if needed

```bash
FILE=docs/README-${{ steps.select.outputs.basename }}.md
if [ ! -f "$FILE" ]; then
  echo "Creating template at $FILE"
  echo "# Documentation for ${{ steps.select.outputs.basename }}" > "$FILE"
  echo "" >> "$FILE"
# ... (truncated)
```

#### 5. Run auto-doc

```yaml
uses: tj-actions/auto-doc@v3
with:
  filename: ${{ steps.select.outputs.workflow_file }}
  reusable: True
  output: docs/README-${{ steps.select.outputs.basename }}.md
```

#### 6. Commit README changes

```yaml
uses: stefanzweifel/git-auto-commit-action@v5
with:
  commit_message: docs: auto-generate README for ${{ steps.select.outputs.base...
  file_pattern: docs/*
```

#### 7. Show result

```bash
echo "==== README OUTPUT ===="
cat docs/README-${{ steps.select.outputs.basename }}.md
echo "========================"
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
