# 📝 📝 Generate/Update README Documentation

**Generated:** 2025-11-25 14:50:21 UTC

---

## Overview

**Workflow File:** `.github/workflows/generate-readme-test.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `detect-changes`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `matrix`: `${{ steps.handle_matrix.outputs.matrix }}`
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
     - `files`: `.github/workflows/ci-*.yml
!.github/workflows/ci-readme-docs.yml
`

3. **Print changed workflow files**
   - 💻 Run: `echo "Changed workflow files:" for f in ${{ steps.detect.outputs.all_changed_files }}; do   echo " - $f" done...`

4. **Prepare matrix**
   - 💻 Run: `files="${{ steps.detect.outputs.all_changed_files }}"  json="[" sep="" for f in $files; do   base=$(basename "$f" .yml) ...`

5. **Handle empty matrix**
   - 💻 Run: `if [ "${{ steps.detect.outputs.any_changed }}" = "false" ]; then   echo "No changes. Injecting dummy matrix item."   ech...`

6. **Get PR source branch**
   - 💻 Run: `echo "pr_source_branch=${{ github.head_ref }}" >> $GITHUB_OUTPUT...`

### `update-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`
     - `token`: `${{ secrets.GITHUB_TOKEN }}`

2. **Create missing READMEs**
   - 💻 Run: `TEMPLATE="docs/README-reusable.md" readme="docs/README-${{ matrix.item.basename }}.md"  if [ ! -f "$readme" ]; then   ec...`

3. **Print newly created README files**
   - 💻 Run: `if [ -n "${{ steps.create_readmes.outputs.new_readmes }}" ]; then   echo "Newly created README files:"   echo "${{ steps...`

4. **Print workflow file from matrix**
   - 💻 Run: `echo "Current workflow file: ${{ matrix.item.workflow }}" echo "Current readme file: docs/${{ matrix.item.basename }}"...`

5. **Auto-doc for workflow**
   - 📦 Action: `tj-actions/auto-doc@v3`
   - ⚙️ Config:
     - `filename`: `./${{ matrix.item.workflow }}`
     - `reusable`: `True`
     - `output`: `docs/README-${{ matrix.item.basename }}.md`
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

6. **Verify changed README**
   - 📦 Action: `tj-actions/verify-changed-files@v19`
   - ⚙️ Config:
     - `files`: `docs/README-${{ matrix.item.basename }}.md`

7. **Print verification result**
   - 💻 Run: `if [ "${{ steps.verify.outputs.files_changed }}" == "true" ]; then   echo "✅ README updated: docs/README-${{ matrix.item...`

8. **Print target branch**
   - 💻 Run: `echo "*** branch *** " ${{ needs.detect-changes.outputs.pr_source_branch }}...`

9. **Create Pull Request for Documentation Update**
   - 📦 Action: `peter-evans/create-pull-request@v6`
   - ⚙️ Config:
     - `commit-message`: `docs: auto-update README for ${{ matrix.item.basename }}`
     - `title`: `docs: auto-update README for ${{ matrix.item.basename }}`
     - `body`: `This PR was automatically generated to update the documentation for workflow `${{ matrix.item.basename }}`.`
     - `branch`: `auto-doc/update-readme-${{ matrix.item.basename }}`
     - `token`: `${{ env.GITHUB_USER_TOKEN }}`
     - `committer`: `${{ env.GITHUB_USER_NAME }} <${{ env.GITHUB_USER_EMAIL }}>`
     - `base`: `${{ needs.detect-changes.outputs.pr_source_branch || github.event.pull_request.base.ref }}`

---

*This documentation is auto-generated. Do not edit manually.*
