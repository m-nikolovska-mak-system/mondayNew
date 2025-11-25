# 📝 Checkout on Release Workflow

## Overview

**Workflow Name:** `Checkout on Release`

## Triggers


## Jobs

### `checkout`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code at release tag**
   - Uses: `actions/checkout@v4`
2. **Show current commit and tag**
   - Runs: `echo "Checked out tag: ${{ github.event.release.tag_name }}"...`

---

*This documentation is auto-generated. Do not edit manually.*
