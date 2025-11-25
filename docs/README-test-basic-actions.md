# 📝 Test Basic Actions (Optimized) Workflow

## Overview

**Workflow Name:** `Test Basic Actions (Optimized)`

## Triggers


## Jobs

### `validate_readme`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Sparse checkout (README only!)**
   - Uses: `actions/checkout@v4`
2. **Run README Validator**
   - Uses: `./.github/actions/readme-validator`

### `lint_check`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Sparse checkout (only what we need to lint)**
   - Uses: `actions/checkout@v4`
2. **Run Linting Check**
   - Uses: `./.github/actions/lint-check`

---

*This documentation is auto-generated. Do not edit manually.*
