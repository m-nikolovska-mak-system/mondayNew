# 📝 📝 Generate/Update README Documentation

**Generated:** 2025-11-27 09:41:14

---

## Overview

**Workflow Name:** `📝 Generate/Update README Documentation`

## Triggers

*No triggers defined*

## 🔨 Jobs

### `detect-changes`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `matrix`: `${{ steps.prep_matrix.outputs.matrix }}`
- `pr_source_branch`: `${{ steps.get_source_branch.outputs.pr_source_branch }}`

**Steps:**

1. **Checkout**
   - 📦 Action: `actions/checkout@v4`

2. **Detect changed workflow files**
   - 📦 Action: `tj-actions/changed-files@v44`
   - ⚙️ Config:
     - `files`: `.github/workflows/*.yml !.github/workflows/generat...`

3. **Stop if no workflows changed**
   - 💻 Run: `echo "No workflow changes detected. Skipping documentation."...`

4. **Prepare matrix JSON**
   - 💻 Run: `json="[]"...`

5. **Get PR source branch**
   - 💻 Run: `echo "pr_source_branch=${{ github.head_ref }}" >> $GITHUB_OU...`

### `update-doc`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0...`
     - `token`: `${{ env.GITHUB_USER_TOKEN }}...`

2. **Install yq (YAML parser)**
   - 💻 Run: `sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah...`

3. **Create custom documentation script**
   - 💻 Run: `cat > generate_docs.sh << 'SCRIPT_EOF'...`

4. **Create missing READMEs from template**
   - 💻 Run: `TEMPLATE="docs/README-reusable.md"...`

5. **Generate documentation**
   - 💻 Run: `./generate_docs.sh \...`

6. **Verify changed README**
   - 📦 Action: `tj-actions/verify-changed-files@v19`
   - ⚙️ Config:
     - `files`: `docs/README-${{ matrix.item.basename }}.md...`

7. **Print verification result**
   - 💻 Run: `if [ "${{ steps.verify.outputs.files_changed }}" == "true" ]...`

8. **Create Pull Request for Documentation Update**
   - 📦 Action: `peter-evans/create-pull-request@v6`
   - ⚙️ Config:
     - `commit-message`: `docs: auto-update README for ${{ matrix.item.basen...`
     - `title`: `docs: auto-update README for ${{ matrix.item.basen...`
     - `body`: `This PR was automatically generated to update the ...`

---

*This documentation is auto-generated. Do not edit manually.*
