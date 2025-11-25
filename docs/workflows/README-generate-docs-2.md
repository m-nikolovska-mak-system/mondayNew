# 📝 Generate Docs

**Generated:** 2025-11-25 14:14:14 UTC

---

## Overview

**Workflow File:** `.github/workflows/generate-docs-2.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `generate-docs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - 📦 Action: `actions/checkout@v4`

2. **Set up Python**
   - 📦 Action: `actions/setup-python@v5`
   - ⚙️ Config:
     - `python-version`: `3.11`

3. **Install dependencies**
   - 💻 Run: `pip install pyyaml...`

4. **Run documentation generator**
   - 💻 Run: `python scripts/generate_docs.py...`

5. **Commit and push changes**
   - 💻 Run: `git config --global user.name "github-actions[bot]" git config --global user.email "github-actions[bot]@users.noreply.gi...`

---

*This documentation is auto-generated. Do not edit manually.*
