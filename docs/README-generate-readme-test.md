# 📝 📝 Generate/Update README Documentation Workflow

## Overview

**Workflow Name:** `📝 Generate/Update README Documentation`

## Triggers


## Jobs

### `detect-changes`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - Uses: `actions/checkout@v4`
2. **Detect changed workflow files**
   - Uses: `tj-actions/changed-files@v44`
3. **Print changed workflow files**
   - Runs: `echo "Changed workflow files:"...`
4. **Prepare matrix**
   - Runs: `files="${{ steps.detect.outputs.all_changed_files }}"...`
5. **Handle empty matrix**
   - Runs: `if [ "${{ steps.detect.outputs.any_changed }}" = "false" ]; ...`
6. **Get PR source branch**
   - Runs: `echo "pr_source_branch=${{ github.head_ref }}" >> $GITHUB_OU...`

### `update-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - Uses: `actions/checkout@v4`
2. **Create missing READMEs**
   - Runs: `TEMPLATE="docs/README-reusable.md"...`
3. **Print newly created README files**
   - Runs: `if [ -n "${{ steps.create_readmes.outputs.new_readmes }}" ];...`
4. **Print workflow file from matrix**
   - Runs: `echo "Current workflow file: ${{ matrix.item.workflow }}"...`
5. **Auto-doc for workflow**
   - Uses: `tj-actions/auto-doc@v3`
6. **Verify changed README**
   - Uses: `tj-actions/verify-changed-files@v19`
7. **Print verification result**
   - Runs: `if [ "${{ steps.verify.outputs.files_changed }}" == "true" ]...`
8. **Print target branch**
   - Runs: `echo "*** branch *** " ${{ needs.detect-changes.outputs.pr_s...`
9. **Create Pull Request for Documentation Update**
   - Uses: `peter-evans/create-pull-request@v6`

---

*This documentation is auto-generated. Do not edit manually.*
