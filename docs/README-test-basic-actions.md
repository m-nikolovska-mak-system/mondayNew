<div align="center">

# 🚀 Test Basic Actions (Optimized)

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/test-basic-actions.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `validate_readme`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Sparse checkout (README only!)

```yaml
uses: actions/checkout@v4
with:
  sparse-checkout: README.md 
  sparse-checkout-cone-mode: False
```

#### 2. Run README Validator

```yaml
uses: ./.github/actions/readme-validator
with:
  min_lines: 5
```

</details>

### 🎯 `lint_check`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Sparse checkout (only what we need to lint)

```yaml
uses: actions/checkout@v4
with:
  sparse-checkout: src/ scripts/ .github/actions/lint-check/ 
  sparse-checkout-cone-mode: False
```

#### 2. Run Linting Check

```yaml
uses: ./.github/actions/lint-check
with:
  file: .
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
