# 📝 Detect File Change

**Generated:** 2025-11-25 14:05:41

---

## Overview

**Workflow Name:** `Detect File Change`

## Triggers

*No triggers defined*

## 🔨 Jobs

### `detect`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `found`: `${{ steps.result.outputs.found }}`
- `files`: `${{ steps.result.outputs.files }}`

**Steps:**

1. **Step 1**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `fetch-depth`: `0...`

2. **Detect changed files**
   - 💻 Run: `set -e...`

---

*This documentation is auto-generated. Do not edit manually.*
