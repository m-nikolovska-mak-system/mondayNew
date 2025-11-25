# 📝 Checkout on Release

**Generated:** 2025-11-25 14:45:12 UTC

---

## Overview

**Workflow File:** `.github/workflows/checkout-on-release.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `checkout`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code at release tag**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `ref`: `${{ github.event.release.tag_name }}`

2. **Show current commit and tag**
   - 💻 Run: `echo "Checked out tag: ${{ github.event.release.tag_name }}" git log -1...`

---

*This documentation is auto-generated. Do not edit manually.*
