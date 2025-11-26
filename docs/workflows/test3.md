# test3.yml

**Source:** `test3.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### greet

| name | action | run |
| --- | --- | --- |
| Print greeting |  | `run` command |

## Full YAML
```yaml
on:
  workflow_dispatch:
    inputs:
      NAME:
        description: "Your name"
        type: string
      GREETING:
        description: "Greeting message"
        type: string

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Print greeting
        run: echo "${{ github.event.inputs.GREETING }}, ${{ github.event.inputs.NAME }}!"

```