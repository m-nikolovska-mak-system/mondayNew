# Test Composite Action

**Source:** `test2.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### test-readme-validator

| name | action | run |
| --- | --- | --- |
| actions/checkout@v3 | actions/checkout@v3 |  |
| Run README Validator | ./actions/readme-validator |  |

## Full YAML
```yaml
name: Test Composite Action

on:
  workflow_dispatch:

jobs:
  test-readme-validator:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run README Validator
        uses: ./actions/readme-validator
        with:
          input_file: README.md
```