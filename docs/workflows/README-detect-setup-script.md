# 📝 Detect Setup Script

**Generated:** 2025-11-25 14:37:06 UTC

---

## Overview

**Workflow File:** `.github/workflows/detect-setup-script.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `detect-iss`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `setup_script`: `${{ steps.detect.outputs.script }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`

2. **Detect .iss setup script**
   - 💻 Run: `file=$(ls *.iss 2>/dev/null | head -n 1) if [ -z "$file" ]; then   echo "❌ No .iss setup script found!"   exit 1 fi echo...`

---

*This documentation is auto-generated. Do not edit manually.*
