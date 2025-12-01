# Reusable Builder THIS IS TO TEST WF CALL !!!!!!!!!!!!!!!!!!

> **Type:** Reusable Workflow  
> **Source:** `test-reusable.yml`

## 📋 Overview

This document provides comprehensive documentation for the `Reusable Builder THIS IS TO TEST WF CALL !!!!!!!!!!!!!!!!!!` workflow.

---

## 🎯 Triggers

- **`workflow_call`**

---

## 📥 Inputs

| Name | Type | Required | Default | Description |
| ---- | ---- | -------- | ------- | ----------- |
| `version` | `string` | ✅ Yes | `_not set_` | Application version |
| `optimize` | `boolean` | ❌ No | `False` | _No description provided_ |

---

## 📤 Outputs

| Name | Description | Value |
| ---- | ----------- | ----- |
| `build_path` | Path where the build artifact is stored | `${{ jobs.build.outputs.path }}` |

---

## 🔐 Secrets

| Name | Required | Description |
| ---- | -------- | ----------- |
| `API_KEY` | ✅ Yes | Secret build key |

---

## 💼 Jobs

### 🔧 `build`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run |
| ---- | ---- | --- |
| Build |  | `echo "path=/tmp/app-${{ inputs.version }}" >> $GITHUB_OUTPUT` |


---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: Reusable Builder THIS IS TO TEST WF CALL !!!!!!!!!!!!!!!!!!

on:
  workflow_call:
    inputs:
      version:
        type: string
        required: true
        description: "Application version"
      optimize:
        type: boolean
        default: false
    secrets:
      API_KEY:
        required: true
        description: "Secret build key"
    outputs:
      build_path:
        description: "Path where the build artifact is stored"
        value: ${{ jobs.build.outputs.path }}

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      path: ${{ steps.build_step.outputs.path }}
    steps:
      - name: Build
        id: build_step
        run: |
          echo "path=/tmp/app-${{ inputs.version }}" >> $GITHUB_OUTPUT
```

</details>

---

**Generated on:** 2025-12-01 10:24:24 UTC
