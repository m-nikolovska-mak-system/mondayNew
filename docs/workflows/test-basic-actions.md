# Test Basic Actions (Optimized)

**Source:** `test-basic-actions.yml`

## Triggers
- `workflow_dispatch`
- `push`
- `pull_request`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### validate_readme

| name | action | run |
| --- | --- | --- |
| Sparse checkout (README only!) | actions/checkout@v4 |  |
| Run README Validator | ./.github/actions/readme-validator |  |

### lint_check

| name | action | run |
| --- | --- | --- |
| Sparse checkout (only what we need to lint) | actions/checkout@v4 |  |
| Run Linting Check | ./.github/actions/lint-check |  |

## Full YAML
```yaml
name: Test Basic Actions (Optimized)

on:
  workflow_dispatch:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate_readme:
    runs-on: ubuntu-latest
    steps:
      - name: Sparse checkout (README only!)
        uses: actions/checkout@v4
        with:
          sparse-checkout: |
            README.md
          sparse-checkout-cone-mode: false
      
      - name: Run README Validator
        uses: ./.github/actions/readme-validator
        with:
          min_lines: 5

  lint_check:
    runs-on: ubuntu-latest
    steps:
      - name: Sparse checkout (only what we need to lint)
        uses: actions/checkout@v4
        with:
          sparse-checkout: |
            src/
            scripts/
            .github/actions/lint-check/
          sparse-checkout-cone-mode: false
      
      - name: Run Linting Check
        uses: ./.github/actions/lint-check
        with:
          file: .
```