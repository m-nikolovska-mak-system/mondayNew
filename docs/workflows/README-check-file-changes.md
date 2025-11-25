# 📝 Check File Changes

**Generated:** 2025-11-25 14:06:40 UTC

---

## Overview

**Workflow File:** `.github/workflows/check-file-changes.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `check`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `changed`: `${{ steps.detect.outputs.changed }}`
- `files`: `${{ steps.detect.outputs.files }}`
- `current_ref`: `${{ steps.refs.outputs.current }}`

**Steps:**

1. **Checkout repository**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0`

2. **Resolve refs**
   - 💻 Run: `current="${{ inputs.current_ref }}" previous="${{ inputs.previous_ref }}"  # Auto-detect current ref if [ -z "$current" ...`

3. **Detect changes**
   - 💻 Run: `pattern="${{ inputs.file_pattern }}" prev="${{ steps.refs.outputs.previous }}" curr="${{ steps.refs.outputs.current }}" ...`

---

*This documentation is auto-generated. Do not edit manually.*
