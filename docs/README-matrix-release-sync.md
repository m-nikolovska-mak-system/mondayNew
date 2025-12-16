# Test - File Detection Only

> **Type:** Manual Dispatch + Automated  
> **Source:** `matrix-release-sync.yml`

## 📋 Overview

This document provides comprehensive documentation for the `Test - File Detection Only` workflow.

---

## 🎯 Triggers

- **`workflow_dispatch`**
- **`release`**
  - Types: `published`

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

### 🔧 `test-detection`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run |
| ---- | ---- | --- |
| Checkout repository | `actions/checkout@v4` | `` |
| Show repo structure |  | ✅ Yes (see full YAML) |
| Check for config file |  | ✅ Yes (see full YAML) |
| Install yq |  | ✅ Yes (see full YAML) |
| Parse config |  | ✅ Yes (see full YAML) |
| Check if source files exist |  | ✅ Yes (see full YAML) |
| Test git diff (for changed mode) |  | ✅ Yes (see full YAML) |
| Summary |  | ✅ Yes (see full YAML) |


---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
# ========================================
# MINIMAL TEST - Just check if files exist
# ========================================
# This workflow just lists what it finds
# No syncing, no errors, just information

name: Test - File Detection Only

on:
  workflow_dispatch:  # Run manually for testing
  release:
    types: [published]

jobs:
  test-detection:
    name: Test File Detection
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Show repo structure
        run: |
          echo "=== Repository Structure ==="
          find . -type f -not -path './.git/*' | head -50
      
      - name: Check for config file
        run: |
          echo "=== Config File ==="
          if [ -f .github/sync-config.yml ]; then
            echo "✅ Config file exists"
            echo ""
            echo "Contents:"
            cat .github/sync-config.yml
          else
            echo "❌ Config file NOT found at .github/sync-config.yml"
            exit 1
          fi
      
      - name: Install yq
        run: |
          sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
          sudo chmod +x /usr/local/bin/yq
      
      - name: Parse config
        run: |
          echo "=== Parsing Config ==="
          
          CONFIG_FILE=".github/sync-config.yml"
          
          echo "Destination repo:"
          yq eval '.destination_repo' $CONFIG_FILE
          
          echo ""
          echo "Mappings:"
          yq eval '.mappings' $CONFIG_FILE
          
          echo ""
          echo "Mappings as JSON:"
          yq eval -o=json '.mappings' $CONFIG_FILE
      
      - name: Check if source files exist
        run: |
          echo "=== Checking Source Files ==="
          
          CONFIG_FILE=".github/sync-config.yml"
          
          # Get all source patterns from all mappings
          yq eval -o=json '.mappings[].source[]' $CONFIG_FILE | while read -r file; do
            # Remove quotes
            file=$(echo $file | tr -d '"')
            
            if [ -f "$file" ]; then
              echo "✅ Found: $file"
            else
              echo "❌ Missing: $file"
              
              # Try to find similar files
              BASENAME=$(basename "$file")
              echo "   Looking for similar files named '$BASENAME':"
              find . -name "$BASENAME" -type f | head -5 | sed 's/^/     /'
            fi
          done
      
      - name: Test git diff (for changed mode)
        run: |
          echo "=== Testing Git Diff ==="
          
          git fetch --tags
          
          LATEST="${{ github.event.release.tag_name }}"
          PREVIOUS=$(git describe --tags --abbrev=0 ${LATEST}^ 2>/dev/null || echo "")
          
          if [ -z "$PREVIOUS" ]; then
            echo "ℹ️  First release (no previous tag)"
            echo ""
            echo "All tracked files:"
            git ls-files | head -20
          else
            echo "Previous tag: $PREVIOUS"
            echo "Latest tag: $LATEST"
            echo ""
            echo "Changed files:"
            git diff --name-only $PREVIOUS $LATEST
          fi
      
      - name: Summary
        if: always()
        run: |
          echo "## 🔍 Test Results" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "If you see this, the workflow structure is valid!" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "Check the logs above for:" >> $GITHUB_STEP_SUMMARY
          echo "- ✅ Config file exists" >> $GITHUB_STEP_SUMMARY
          echo "- ✅ Source files exist" >> $GITHUB_STEP_SUMMARY
          echo "- ✅ Git diff works" >> $GITHUB_STEP_SUMMARY
```

</details>

---

**Generated on:** 2025-12-16 09:48:46 UTC
