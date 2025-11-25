# 📝 Generate Docs Workflow

## Overview

**Workflow Name:** `Generate Docs`

## Triggers


## Jobs

### `generate-docs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - Uses: `actions/checkout@v4`
2. **Set up Python**
   - Uses: `actions/setup-python@v5`
3. **Install dependencies**
   - Runs: `pip install pyyaml...`
4. **Run documentation generator**
   - Runs: `python scripts/generate_docs.py...`
5. **Commit and push changes**
   - Runs: `git config --global user.name "github-actions[bot]"...`

---

*This documentation is auto-generated. Do not edit manually.*
