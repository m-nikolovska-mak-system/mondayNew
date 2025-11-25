<div align="center">

# 🚀 Advanced ACT Test

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/advanced-test.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `test-matrix`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Setup Node.js ${{ matrix.node }}

```yaml
uses: actions/setup-node@v3
with:
  node-version: ${{ matrix.node }}
```

#### 2. Print Environment

```bash
echo "Running on ${{ matrix.os }} with Node.js ${{ matrix.node }}"
```

</details>

### 🎯 `validate-inputs`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Check dry-run input

```bash
if [[ "${{ github.event.inputs.dry_run }}" == "true" ]]; then
  echo "Dry run mode enabled"
else
  echo "Executing real changes"
fi
```

</details>

### 🎯 `use-secrets`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Print secret (simulated)

```bash
echo "Secret is set (not printing for safety)"
```

</details>

### 🎯 `conditional-step`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Run only in dev

```bash
echo "Running in development environment"
```

</details>

### 🎯 `concurrency-test`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Simulate long task

```bash
sleep 10
```

</details>

### 🎯 `post-run-cleanup`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Setup

```bash
echo "Setting up resources"
```

#### 2. Cleanup

```bash
echo "Cleaning up resources"
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:20 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
