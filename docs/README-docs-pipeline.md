# 🚀 Complete Docs Pipeline (Orchestrator)

> **Type:** Manual Dispatch + Automated  
> **Source:** `docs-pipeline.yml`

## 📋 Overview

This document provides comprehensive documentation for the `🚀 Complete Docs Pipeline (Orchestrator)` workflow.

---

## 🎯 Triggers

- **`workflow_dispatch`**
- **`push`**
  - Branches: `main`
  - Paths (includes): `docs/**, .github/workflows/*.yml, .github/workflows/*.yaml`

---

## 📥 Inputs

_This workflow does not accept any inputs._

---

## 📤 Outputs

_This workflow does not expose any outputs._

---

## 🔐 Secrets

_This workflow does not require any secrets._

---

## 💼 Jobs

### 🔧 `generate-readmes`

_No steps defined._

### 🔧 `sync-to-confluence`

_No steps defined._

### 🔧 `update-database`

_No steps defined._

### 🔧 `notify-completion`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run |
| ---- | ---- | --- |
| Report status |  | ✅ Yes (see full YAML) |


---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: 🚀 Complete Docs Pipeline (Orchestrator)

on:
  workflow_dispatch:  # Manual trigger
  push:
    branches: [ main ]
    paths:
      - 'docs/**'
      - '.github/workflows/*.yml'
      - '.github/workflows/*.yaml'

permissions:
  contents: write
  pull-requests: write

jobs:
  # ============================================
  # STEP 1: Generate READMEs from workflow files
  # ============================================
  generate-readmes:
    name: 📝 Step 1 - Generate READMEs
    uses: ./.github/workflows/new-ci-readme-docs.yml
    secrets: inherit

  # ============================================
  # STEP 2: Upload docs to Confluence
  # ============================================
  sync-to-confluence:
    name: 🔄 Step 2 - Sync to Confluence
    needs: generate-readmes
    uses: ./.github/workflows/auto-confluence-v3.yml
    secrets: inherit

  # ============================================
  # STEP 3: Update Confluence database with page IDs
  # ============================================
  update-database:
    name: 📊 Step 3 - Update Database
    needs: sync-to-confluence
    if: needs.sync-to-confluence.outputs.page_mappings != '{}'
    uses: ./.github/workflows/update-confluence-db.yml
    with:
      page_mappings: ${{ needs.sync-to-confluence.outputs.page_mappings }}
    secrets: inherit

  # ============================================
  # FINAL NOTIFICATION
  # ============================================
  notify-completion:
    name: 🎉 Pipeline Complete
    needs: [generate-readmes, sync-to-confluence, update-database]
    if: always()
    runs-on: ubuntu-latest
    steps:
      - name: Report status
        run: |
          echo "### 📊 Pipeline Status Report"
          echo "- Generate READMEs: ${{ needs.generate-readmes.result }}"
          echo "- Sync to Confluence: ${{ needs.sync-to-confluence.result }}"
          echo "- Update Database: ${{ needs.update-database.result }}"
          
          if [ "${{ needs.update-database.result }}" == "success" ]; then
            echo "::notice::🎉 Complete pipeline executed successfully!"
          else
            echo "::warning::⚠️ Pipeline completed with some issues. Check individual steps above."
          fi
```

</details>

---

**Generated on:** 2025-12-03 13:51:10 UTC
