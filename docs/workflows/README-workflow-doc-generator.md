# 📝 Generate Workflow Documentation

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/workflow-doc-generator.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `generate-docs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`

2. **Setup Python**
   - 📦 Action: `actions/setup-python@v5`
   - ⚙️ Config:
     - `python-version`: `3.11`

3. **Install dependencies**
   - 💻 Run: `pip install pyyaml...`

4. **List all workflows**
   - 💻 Run: `echo "=== All workflow files ===" find .github/workflows -name "*.yml" -o -name "*.yaml" echo "=========================...`

5. **Generate documentation**
   - 💻 Run: `mkdir -p docs  cat > generate_docs.py << 'EOF' import yaml import sys from pathlib import Path from datetime import date...`

6. **Show generated docs**
   - 💻 Run: `echo "==== GENERATED DOCUMENTATION ====" for file in docs/README-*.md; do   if [ -f "$file" ]; then     echo ""     echo...`

7. **Create Pull Request**
   - 📦 Action: `peter-evans/create-pull-request@v6`
   - ⚙️ Config:
     - `token`: `${{ secrets.GITHUB_TOKEN }}`
     - `commit-message`: `docs: auto-generate workflow documentation`
     - `title`: `📝 Update Workflow Documentation`
     - `body`: `## 🤖 Auto-generated Documentation Update

This PR contains automatically generated documentation for all workflows.

### 📄 Generated Docs
Check the `docs/` folder for updated README files.

---
*This is an automated PR. Review before merging.*
`
     - `branch`: `docs/workflow-update-${{ github.run_number }}`
     - `delete-branch`: `True`
     - `labels`: `documentation
automated
`

---

*This documentation is auto-generated. Do not edit manually.*
