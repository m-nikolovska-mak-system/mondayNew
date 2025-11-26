# Test Act Workflow

**Source:** `test.yml`

## Triggers
- `push`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### test

| name | action | run |
| --- | --- | --- |
| Checkout code | actions/checkout@v3 |  |
| Say Hello |  | `run` command |
| Validate README | ./.github/actions/readme-check |  |

## Full YAML
```yaml
name: Test Act Workflow
on: push

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Say Hello
        run: echo "Hello from Act!"

      - name: Validate README
        uses: ./.github/actions/readme-check
```