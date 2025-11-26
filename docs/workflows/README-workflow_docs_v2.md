# 📝 📝 Auto-generate workflow READMEs v5

**Generated:** 2025-11-26 12:27:54 UTC

---

## Overview

**Workflow File:** `.github/workflows/workflow_docs_v2.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `detect-changes`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `matrix`: `${{ steps.handle_matrix.outputs.matrix }}`
- `has_changes`: `${{ steps.handle_matrix.outputs.has_changes }}`
- `pr_source_branch`: `${{ steps.get_source_branch.outputs.pr_source_branch }}`

**Steps:**

1. **Checkout**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`
     - `token`: `${{ secrets.GITHUB_TOKEN }}`

2. **Detect changed workflow files**
   - 📦 Action: `tj-actions/changed-files@v44`
   - ⚙️ Config:
     - `files`: `.github/workflows/*.yml
!.github/workflows/workflow_docs_v2.yml
`

3. **Prepare matrix**
   - 💻 Run: `files="${{ steps.detect.outputs.all_changed_files }}" json="[" sep="" for f in $files; do   base=$(basename "$f" .yml)  ...`

4. **Handle empty matrix**
   - 💻 Run: `if [ "${{ steps.detect.outputs.any_changed }}" = "false" ]; then   echo 'matrix={"include":[]}' >> $GITHUB_OUTPUT   echo...`

5. **Get PR source branch**
   - 💻 Run: `echo "pr_source_branch=${{ github.head_ref || github.ref_name }}" >> $GITHUB_OUTPUT`

### `update-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`
     - `token`: `${{ secrets.GITHUB_TOKEN }}`

2. **Ensure docs folder**
   - 💻 Run: `mkdir -p docs`

3. **Auto-doc for workflow**
   - 📦 Action: `tj-actions/auto-doc@v3`
   - ⚙️ Config:
     - `filename`: `./${{ matrix.workflow }}`
     - `reusable`: `True`
     - `output`: `docs/README-${{ matrix.basename }}.md`
     - `inputs`: `True`
     - `outputs`: `True`
     - `steps`: `detailed`
     - `include_html`: `True`
     - `use_code_blocks`: `True`
     - `markdown_links`: `True`
     - `markdown_format`: `rich`
     - `badges`: `True`
     - `col_max_width`: `200`
     - `col_max_words`: `999`

4. **Verify changed README**
   - 📦 Action: `tj-actions/verify-changed-files@v19`
   - ⚙️ Config:
     - `files`: `docs/README-${{ matrix.basename }}.md`

5. **Create Pull Request for Documentation Update**
   - 📦 Action: `peter-evans/create-pull-request@v6`
   - ⚙️ Config:
     - `commit-message`: `docs: auto-update README for ${{ matrix.basename }}`
     - `title`: `docs: auto-update README for ${{ matrix.basename }}`
     - `body`: `This PR auto-updates the documentation for workflow `${{ matrix.basename }}`.`
     - `branch`: `auto-doc/update-readme-${{ matrix.basename }}`
     - `token`: `${{ env.GITHUB_USER_TOKEN }}`
     - `committer`: `${{ env.GITHUB_USER_NAME }} <${{ env.GITHUB_USER_EMAIL }}>`
     - `base`: `${{ needs.detect-changes.outputs.pr_source_branch }}`

---

*This documentation is auto-generated. Do not edit manually.*
