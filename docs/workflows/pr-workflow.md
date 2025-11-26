# Test PR Workflow

**Source:** `pr-workflow.yml`

## Triggers
- `pull_request`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### print-info

| name | action | run |
| --- | --- | --- |
| Show PR info |  | `run` command |

## Full YAML
```yaml
name: Test PR Workflow

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  print-info:
    runs-on: ubuntu-latest
    steps:
      - name: Show PR info
        run: |
          echo "PR base branch: ${{ github.event.pull_request.base.ref }}"
          echo "PR head branch: ${{ github.event.pull_request.head.ref }}"

```