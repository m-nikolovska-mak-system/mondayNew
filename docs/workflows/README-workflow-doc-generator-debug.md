# 📝 Generate Workflow Documentation (Debug)

**Generated:** 2025-11-25 14:37:06 UTC

---

## Overview

**Workflow File:** `.github/workflows/workflow-doc-generator-debug.yml`

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

2. **Debug - Check repo structure**
   - 💻 Run: `echo "=== Repository Structure ===" ls -la echo "" echo "=== Workflow files ===" ls -la .github/workflows/ echo "" echo ...`

3. **Setup Python**
   - 📦 Action: `actions/setup-python@v5`
   - ⚙️ Config:
     - `python-version`: `3.11`

4. **Install dependencies**
   - 💻 Run: `echo "Installing PyYAML..." pip install pyyaml echo "Done!"...`

5. **Debug - List all workflows**
   - 💻 Run: `echo "=== Finding workflow files ===" find .github/workflows -type f \( -name "*.yml" -o -name "*.yaml" \) echo "" echo ...`

6. **Debug - Test Python and PyYAML**
   - 💻 Run: `echo "Testing Python..." python --version echo "" echo "Testing PyYAML import..." python -c "import yaml; print('PyYAML ...`

7. **Generate documentation**
   - 💻 Run: `mkdir -p docs  cat > generate_docs.py << 'END_OF_PYTHON' import yaml import sys from pathlib import Path from datetime i...`

8. **Show generated docs**
   - 💻 Run: `echo "==== GENERATED DOCUMENTATION ====" for file in docs/README-*.md; do   if [ -f "$file" ]; then     echo ""     echo...`

9. **Create Pull Request**
   - 📦 Action: `peter-evans/create-pull-request@v6`
   - ⚙️ Config:
     - `token`: `${{ secrets.GITHUB_TOKEN }}`
     - `commit-message`: `docs: auto-generate workflow documentation`
     - `title`: `📝 Update Workflow Documentation (Debug)`
     - `body`: `## 🤖 Debug Documentation Update

This is a debug run to see what's being generated.

Check the workflow logs and generated files.
`
     - `branch`: `docs/workflow-debug-${{ github.run_number }}`
     - `delete-branch`: `True`

---

*This documentation is auto-generated. Do not edit manually.*
