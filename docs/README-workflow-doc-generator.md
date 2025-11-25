# 📝 Generate Workflow Documentation Workflow

## Overview

**Workflow Name:** `Generate Workflow Documentation`

## Triggers


## Jobs

### `generate-docs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout**
   - Uses: `actions/checkout@v4`
2. **Detect changed workflows**
   - Runs: `# Get list of changed workflow files...`
3. **Setup Python**
   - Uses: `actions/setup-python@v5`
4. **Install dependencies**
   - Runs: `pip install pyyaml...`
5. **Generate documentation**
   - Runs: `mkdir -p docs...`
6. **Create Pull Request**
   - Uses: `peter-evans/create-pull-request@v6`
7. **Show generated docs**
   - Runs: `echo "==== GENERATED DOCUMENTATION ===="...`

---

*This documentation is auto-generated. Do not edit manually.*
