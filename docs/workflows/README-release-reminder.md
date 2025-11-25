# 📝 Notify App Changes on Release

**Generated:** 2025-11-25 14:32:46 UTC

---

## Overview

**Workflow File:** `.github/workflows/release-reminder.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check_app_change`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `should_notify`: `${{ steps.check.outputs.should_notify }}`

**Steps:**

1. **Checkout repository**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`

2. **Get current release tag**
   - 💻 Run: `echo "tag=${{ github.event.release.tag_name }}" >> $GITHUB_OUTPUT...`

3. **Get previous tag**
   - 💻 Run: `prev_tag=$(git tag --sort=-creatordate | grep -B1 "${{ steps.current_tag.outputs.tag }}" | head -n1) echo "prev_tag=$pre...`

4. **Check if App.java changed**
   - 💻 Run: `if git diff --name-only ${{ steps.previous_tag.outputs.prev_tag }} ${{ steps.current_tag.outputs.tag }} | grep -q 'onePr...`

### `notify`

**Runner:** `unknown`

**Steps:**

---

*This documentation is auto-generated. Do not edit manually.*
