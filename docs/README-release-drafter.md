# Release Drafter

> **Type:** Automated  
> **Source:** `release-drafter.yml`

## 📋 Overview

This document provides comprehensive documentation for the `Release Drafter` workflow.

---

## 🎯 Triggers

- **`push`**
  - Branches: `main`
- **`pull_request`**
  - Types: `opened, reopened, synchronize`

---

## 📥 Inputs

_This workflow does not accept any inputs._

---

## 📤 Outputs

_This workflow does not expose any outputs._

---

## 🔐 Secrets

_This workflow does not require any secrets._

---

## 💼 Jobs

### 🔧 `update_release_draft`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run |
| ---- | ---- | --- |
| Step 1 | `release-drafter/release-drafter@v6` | `` |


---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: Release Drafter

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, reopened, synchronize]

permissions:
  contents: read

jobs:
  update_release_draft:
    permissions:
      contents: write
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - uses: release-drafter/release-drafter@v6
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

</details>

---

**Generated on:** 2025-12-12 11:19:01 UTC
