# 📝 Advanced ACT Test Workflow

## Overview

**Workflow Name:** `Advanced ACT Test`

## Triggers


## Jobs

### `test-matrix`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Setup Node.js ${{ matrix.node }}**
   - Uses: `actions/setup-node@v3`
2. **Print Environment**
   - Runs: `echo "Running on ${{ matrix.os }} with Node.js ${{ matrix.no...`

### `validate-inputs`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Check dry-run input**
   - Runs: `if [[ "${{ github.event.inputs.dry_run }}" == "true" ]]; the...`

### `use-secrets`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Print secret (simulated)**
   - Runs: `echo "Secret is set (not printing for safety)"...`

### `conditional-step`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Run only in dev**
   - Runs: `echo "Running in development environment"...`

### `concurrency-test`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Simulate long task**
   - Runs: `sleep 10...`

### `post-run-cleanup`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Setup**
   - Runs: `echo "Setting up resources"...`
2. **Cleanup**
   - Runs: `echo "Cleaning up resources"...`

---

*This documentation is auto-generated. Do not edit manually.*
