# Sync Docs to Confluence v3

> **Type:** Reusable Workflow + Manual Dispatch + Automated  
> **Source:** `auto-confluence-v3.yml`

## 📋 Overview

This document provides comprehensive documentation for the `Sync Docs to Confluence v3` workflow.

---

## 🎯 Triggers

- **`workflow_call`**
- **`workflow_dispatch`**
- **`push`**
  - Branches: `main`
  - Paths (includes): `docs/**`

---

## 📥 Inputs

_This workflow does not accept any inputs._

---

## 📤 Outputs

| Name | Description | Value |
| ---- | ----------- | ----- |
| `page_mappings` | JSON mapping of workflow names to Confluence page IDs | `${{ jobs.sync-docs.outputs.mappings }}` |

---

## 🔐 Secrets

_This workflow does not require any secrets._

---

## 💼 Jobs

### 🔧 `sync-docs`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run |
| ---- | ---- | --- |
| Checkout | `actions/checkout@v4` | `` |
| Detect changed files | `tj-actions/changed-files@v44` | `` |
| Check if docs changed |  | ✅ Yes (see full YAML) |
| List changed docs |  | ✅ Yes (see full YAML) |
| Extract workflow metadata |  | ✅ Yes (see full YAML) |
| Publish Docs to Confluence | `Bhacaz/docs-as-code-confluence@v3` | `` |
| Get Confluence page IDs for all changed docs |  | ✅ Yes (see full YAML) |
| Save mappings for next workflow |  | ✅ Yes (see full YAML) |
| Notify success |  | `echo "::notice::✅ Confluence sync completed successfully!"` |
| Notify failure |  | ✅ Yes (see full YAML) |


---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: Sync Docs to Confluence v3

on:
  workflow_call:  # Can be called by orchestrator
    outputs:
      page_mappings:
        description: "JSON mapping of workflow names to Confluence page IDs"
        value: ${{ jobs.sync-docs.outputs.mappings }}
  workflow_dispatch:  # Can still run manually
  push:
    branches: [ main ]
    paths: [ 'docs/**' ]

permissions:
  contents: read

jobs:
  sync-docs:
    name: 📤 Upload Docs to Confluence
    runs-on: ubuntu-latest
    outputs:
      mappings: ${{ steps.collect_mappings.outputs.json }}
    concurrency:
      group: confluence-sync
      cancel-in-progress: false

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Detect changed files
        id: changed_files
        uses: tj-actions/changed-files@v44
        with:
          files: docs/**

      - name: Check if docs changed
        id: check_changes
        run: |
          if [ "${{ steps.changed_files.outputs.any_changed }}" == "true" ]; then
            echo "changed=true" >> $GITHUB_OUTPUT
            echo "✅ Docs changed - proceeding with sync"
          else
            echo "changed=false" >> $GITHUB_OUTPUT
            echo "⚠️ No changes in docs/ - skipping sync"
          fi

      - name: List changed docs
        if: steps.check_changes.outputs.changed == 'true'
        run: |
          echo "📄 Changed docs files:"
          for f in ${{ steps.changed_files.outputs.all_changed_files }}; do
            echo " - $f"
          done

      - name: Extract workflow metadata
        if: steps.check_changes.outputs.changed == 'true'
        id: meta
        run: |
          FILE=$(echo "${{ steps.changed_files.outputs.all_changed_files }}" | cut -d',' -f1)
          NAME=$(basename "$FILE" .md)
          echo "workflow_name=$NAME" >> $GITHUB_OUTPUT

      - name: Publish Docs to Confluence
        if: steps.check_changes.outputs.changed == 'true'
        id: publish
        uses: Bhacaz/docs-as-code-confluence@v3
        with:
            folder: docs
            username: ${{ secrets.CONFLUENCE_USER }}
            password: ${{ secrets.CONFLUENCE_API_TOKEN }}
            confluence-base-url: ${{ vars.CONFLUENCE_BASE }}
            space-key: DS
            parent-page-id: ${{ secrets.CONFLUENCE_PARENT_PAGE_ID }}
        timeout-minutes: 10

      - name: Get Confluence page IDs for all changed docs
        if: steps.check_changes.outputs.changed == 'true'
        id: get_page_ids
        run: |
          # Create a JSON mapping of workflow name -> page ID
          MAPPINGS="{"
          FIRST=true
          
          for FILE in ${{ steps.changed_files.outputs.all_changed_files }}; do
            # Extract workflow name from filename (e.g., "docs/README-deploy.md" -> "README-deploy")
            TITLE=$(basename "$FILE" .md)
            
            echo "🔍 Looking up page ID for: $TITLE"
            
            # Query Confluence API for page ID
            RESPONSE=$(curl -s -u "${{ secrets.CONFLUENCE_USER }}:${{ secrets.CONFLUENCE_API_TOKEN }}" \
              "${{ vars.CONFLUENCE_BASE }}/rest/api/content?title=${TITLE}&spaceKey=DS")
            
            PAGE_ID=$(echo "$RESPONSE" | jq -r '.results[0].id // "null"')
            
            if [ "$PAGE_ID" != "null" ] && [ -n "$PAGE_ID" ]; then
              echo "✅ Found page ID: $PAGE_ID for $TITLE"
              
              if [ "$FIRST" = false ]; then
                MAPPINGS="$MAPPINGS,"
              fi
              MAPPINGS="$MAPPINGS\"$TITLE\":\"$PAGE_ID\""
              FIRST=false
            else
              echo "⚠️ Could not find page ID for $TITLE"
            fi
          done
          
          MAPPINGS="$MAPPINGS}"
          echo "mappings=$MAPPINGS" >> $GITHUB_OUTPUT
          echo "📋 Final mappings: $MAPPINGS"

      - name: Save mappings for next workflow
        if: steps.check_changes.outputs.changed == 'true'
        id: collect_mappings
        run: |
          MAPPINGS="${{ steps.get_page_ids.outputs.mappings }}"
          echo "json=$MAPPINGS" >> $GITHUB_OUTPUT

      - name: Notify success
        if: steps.check_changes.outputs.changed == 'true' && success()
        run: echo "::notice::✅ Confluence sync completed successfully!"

      - name: Notify failure
        if: failure()
        run: echo "::error::❌ Confluence sync failed. Check the logs above for details."
```

</details>

---

**Generated on:** 2025-12-03 15:02:11 UTC
