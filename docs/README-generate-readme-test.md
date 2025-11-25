<div align="center">

# 🚀 📝 Generate/Update README Documentation

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/generate-readme-test.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `detect-changes`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
matrix: ${{ steps.handle_matrix.outputs.matrix }}
pr_source_branch: ${{ steps.get_source_branch.outputs.pr_source_branch }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 0
  token: ${{ secrets.GITHUB_TOKEN }}
```

#### 2. Detect changed workflow files

```yaml
uses: tj-actions/changed-files@v44
with:
  files: .github/workflows/ci-*.yml !.github/workflows/ci-readme-docs...
```

#### 3. Print changed workflow files

```bash
echo "Changed workflow files:"
for f in ${{ steps.detect.outputs.all_changed_files }}; do
  echo " - $f"
done
```

#### 4. Prepare matrix

```bash
files="${{ steps.detect.outputs.all_changed_files }}"

json="["
sep=""
for f in $files; do
# ... (truncated)
```

#### 5. Handle empty matrix

```bash
if [ "${{ steps.detect.outputs.any_changed }}" = "false" ]; then
  echo "No changes. Injecting dummy matrix item."
  echo 'matrix=[{"workflow":"none","basename":"none"}]' >> $GITHUB_OUTPUT
else
  echo "Matrix already set by prep_matrix."
# ... (truncated)
```

#### 6. Get PR source branch

```bash
echo "pr_source_branch=${{ github.head_ref }}" >> $GITHUB_OUTPUT
```

</details>

### 🎯 `update-doc`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout

```yaml
uses: actions/checkout@v4
with:
  fetch-depth: 0
  token: ${{ secrets.GITHUB_TOKEN }}
```

#### 2. Create missing READMEs

```bash
TEMPLATE="docs/README-reusable.md"
readme="docs/README-${{ matrix.item.basename }}.md"

if [ ! -f "$readme" ]; then
  echo "Creating $readme"
# ... (truncated)
```

#### 3. Print newly created README files

```bash
if [ -n "${{ steps.create_readmes.outputs.new_readmes }}" ]; then
  echo "Newly created README files:"
  echo "${{ steps.create_readmes.outputs.new_readmes }}"
else
  echo "No new README files created."
# ... (truncated)
```

#### 4. Print workflow file from matrix

```bash
echo "Current workflow file: ${{ matrix.item.workflow }}"
echo "Current readme file: docs/${{ matrix.item.basename }}"
```

#### 5. Auto-doc for workflow

```yaml
uses: tj-actions/auto-doc@v3
with:
  filename: ./${{ matrix.item.workflow }}
  reusable: True
  output: docs/README-${{ matrix.item.basename }}.md
```

#### 6. Verify changed README

```yaml
uses: tj-actions/verify-changed-files@v19
with:
  files: docs/README-${{ matrix.item.basename }}.md
```

#### 7. Print verification result

```bash
if [ "${{ steps.verify.outputs.files_changed }}" == "true" ]; then
  echo "✅ README updated: docs/README-${{ matrix.item.basename }}.md"

  # Print the content (should show your Inputs table)
  echo "--- Content ---"
# ... (truncated)
```

#### 8. Print target branch

```bash
echo "*** branch *** " ${{ needs.detect-changes.outputs.pr_source_branch }}
```

#### 9. Create Pull Request for Documentation Update

```yaml
uses: peter-evans/create-pull-request@v6
with:
  commit-message: docs: auto-update README for ${{ matrix.item.basename }}
  title: docs: auto-update README for ${{ matrix.item.basename }}
  body: This PR was automatically generated to update the documentat...
  branch: auto-doc/update-readme-${{ matrix.item.basename }}
  token: ${{ env.GITHUB_USER_TOKEN }}
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
