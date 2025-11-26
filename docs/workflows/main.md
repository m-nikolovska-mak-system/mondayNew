# Test Workflow

**Source:** `main.yml`

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

## Full YAML
```yaml
name: Test Workflow
on: push

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Say Hello
        run: echo "Hello from Act!"
```