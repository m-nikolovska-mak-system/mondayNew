# 📝 Notify App Changes on Release Workflow

## Overview

**Workflow Name:** `Notify App Changes on Release`

## Triggers


## Jobs

### `check_app_change`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout repository**
   - Uses: `actions/checkout@v4`
2. **Get current release tag**
   - Runs: `echo "tag=${{ github.event.release.tag_name }}" >> $GITHUB_O...`
3. **Get previous tag**
   - Runs: `prev_tag=$(git tag --sort=-creatordate | grep -B1 "${{ steps...`
4. **Check if App.java changed**
   - Runs: `if git diff --name-only ${{ steps.previous_tag.outputs.prev_...`

### `notify`

---

*This documentation is auto-generated. Do not edit manually.*
