# 📝 Auto-Generate Workflow Documentation

## 📋 Overview

This document provides comprehensive documentation for the **📝 Auto-Generate Workflow Documentation** workflow.

---

## 🎯 Triggers



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

### `detect-changes`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run Command |
| ---- | ---- | ----------- |
| Checkout | `actions/checkout@v4` |  |
| Detect changed workflow files | `tj-actions/changed-files@v44` |  |
| List changed workflows |  | ✅ Yes (see YAML) |

### `generate-docs`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run Command |
| ---- | ---- | ----------- |
| Checkout | `actions/checkout@v4` |  |
| Set up Python | `actions/setup-python@v5` |  |
| Install PyYAML |  | `pip install pyyaml` |
| Create docs directory |  | `mkdir -p docs` |
| Generate READMEs for changed workflows |  | ✅ Yes (see YAML) |
| Check for changes |  | ✅ Yes (see YAML) |
| Commit and push changes |  | ✅ Yes (see YAML) |

### `summary`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run Command |
| ---- | ---- | ----------- |
| Create summary |  | ✅ Yes (see YAML) |

---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: 📝 Auto-Generate Workflow Documentation

on:
  # Run when workflow files change
#  pull_request:
 #   paths:
  #    - '.github/workflows/*.yml'
   #   - '.github/workflows/*.yaml'
  
  # Also allow manual trigger
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

jobs:
  detect-changes:
    name: 🔍 Detect Changed Workflows
    runs-on: ubuntu-latest
    outputs:
      changed_files: ${{ steps.changed.outputs.all_changed_files }}
      has_changes: ${{ steps.changed.outputs.any_changed }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Need history to detect changes

      - name: Detect changed workflow files
        id: changed
        uses: tj-actions/changed-files@v44
        with:
          files: |
            .github/workflows/*.yml
            .github/workflows/*.yaml
          # Exclude this workflow itself
          files_ignore: |
            .github/workflows/auto-generate-docs.yml

      - name: List changed workflows
        if: steps.changed.outputs.any_changed == 'true'
        run: |
          echo "📋 Changed workflow files:"
          for file in ${{ steps.changed.outputs.all_changed_files }}; do
            echo "  - $file"
          done

  generate-docs:
    name: 📝 Generate Documentation
    needs: detect-changes
    if: needs.detect-changes.outputs.has_changes == 'true'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install PyYAML
        run: pip install pyyaml

      - name: Create docs directory
        run: mkdir -p docs

      - name: Generate READMEs for changed workflows
        run: |
          echo "📝 Generating documentation for changed workflows..."
          
          # Loop through each changed file
          for workflow_file in ${{ needs.detect-changes.outputs.changed_files }}; do
            echo ""
            echo "🔄 Processing: $workflow_file"
            
            # Extract filename without path and extension
            # e.g., .github/workflows/ci-build-jar.yml -> ci-build-jar
            basename=$(basename "$workflow_file" .yml)
            basename=$(basename "$basename" .yaml)
            
            # Generate output filename
            output_file="docs/README-${basename}.md"
            
            echo "   Output: $output_file"
            
            # Run the extractor
            python3 scripts/extract.py "$workflow_file" "$output_file"
            
            echo "   ✅ Done!"
          done
          
          echo ""
          echo "📂 Generated documentation files:"
          ls -lh docs/README-*.md

      - name: Check for changes
        id: git_status
        run: |
          git add docs/
          if git diff --staged --quiet; then
            echo "has_changes=false" >> $GITHUB_OUTPUT
            echo "ℹ️ No documentation changes to commit"
          else
            echo "has_changes=true" >> $GITHUB_OUTPUT
            echo "✅ Documentation changes detected"
          fi

      - name: Commit and push changes
        if: steps.git_status.outputs.has_changes == 'true'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git commit -m "docs: auto-generate workflow documentation"
          git push
          echo "✅ Documentation committed and pushed"

  summary:
    name: 📊 Summary
    needs: [detect-changes, generate-docs]
    if: always()
    runs-on: ubuntu-latest
    steps:
      - name: Create summary
        run: |
          echo "## 📝 Documentation Generation Summary" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          
          if [ "${{ needs.detect-changes.outputs.has_changes }}" == "true" ]; then
            echo "✅ **Workflow changes detected**" >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "Generated documentation for:" >> $GITHUB_STEP_SUMMARY
            for file in ${{ needs.detect-changes.outputs.changed_files }}; do
              basename=$(basename "$file" .yml)
              basename=$(basename "$basename" .yaml)
              echo "- \`$file\` → \`docs/README-${basename}.md\`" >> $GITHUB_STEP_SUMMARY
            done
          else
            echo "ℹ️ **No workflow changes detected**" >> $GITHUB_STEP_SUMMARY
            echo "" >> $GITHUB_STEP_SUMMARY
            echo "No workflows were modified in this PR." >> $GITHUB_STEP_SUMMARY
          fi
```

</details>

---

**Generated on:** 2025-12-01 10:28:26
