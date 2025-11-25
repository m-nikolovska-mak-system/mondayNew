# 📝 Notify Teams on Changes Workflow

## Overview

**Workflow Name:** `Notify Teams on Changes`

## Triggers


## Jobs

### `detect-changes`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Get changed files**
   - Runs: `# For push events, compare with previous commit...`

### `notify-teams`

---

*This documentation is auto-generated. Do not edit manually.*
