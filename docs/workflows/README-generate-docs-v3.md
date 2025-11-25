# 📝 Generate Workflow Documentation

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/generate-docs-v3.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `generate-docs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Step 1**
   - 📦 Action: `actions/checkout@v4`

2. **Step 2**
   - 📦 Action: `actions/setup-python@v5`
   - ⚙️ Config:
     - `python-version`: `3.11`

3. **Step 3**
   - 💻 Run: `pip install pyyaml...`

4. **Generate documentation**
   - 💻 Run: `mkdir -p docs/workflows python scripts/generate-docs-v2.py...`

5. **Check for changes**
   - 💻 Run: `if git diff --quiet docs/; then   echo "changed=false" >> $GITHUB_OUTPUT else   echo "changed=true" >> $GITHUB_OUTPUT...`

6. **Create Pull Request**
   - 📦 Action: `peter-evans/create-pull-request@v6`
   - ⚙️ Config:
     - `commit-message`: `docs: auto-generate workflow documentation`
     - `branch`: `docs/workflow-update-${{ github.run_number }}`
     - `title`: `📝 Update Workflow Documentation`
     - `body`: `## 🤖 Auto-generated Documentation Update
This PR updates workflow documentation in `docs/workflows/`.
`
     - `labels`: `documentation, automated`

---

*This documentation is auto-generated. Do not edit manually.*
