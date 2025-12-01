# Nightly Crons THIS IS TO TEST SCHEDULED !!!!!!!!!

## 📋 Overview

This document provides comprehensive documentation for the **Nightly Crons THIS IS TO TEST SCHEDULED !!!!!!!!!** workflow.

---

## 🎯 Triggers



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

### `run`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run Command |
| ---- | ---- | ----------- |
| Step 1 |  | `echo "Scheduled job running"` |

---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: Nightly Crons THIS IS TO TEST SCHEDULED !!!!!!!!!
on:
  schedule:
    - cron: "0 2 * * *"
    - cron: "30 7 * * 1-5"
  push:
    branches:
      - "main"

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Scheduled job running"
```

</details>

---

**Generated on:** 2025-12-01 10:28:24
