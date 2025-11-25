# 📝 Detect Setup Script Workflow

## Overview

**Workflow Name:** `Detect Setup Script`

## Triggers


## Jobs

### `detect-iss`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Detect .iss setup script**
   - Runs: `file=$(ls *.iss 2>/dev/null | head -n 1)...`

---

*This documentation is auto-generated. Do not edit manually.*
