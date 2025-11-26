# Hello World Workflow

**Source:** `helloo.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### hello

| name | action | run |
| --- | --- | --- |
| Print Hello |  | `run` command |

## Full YAML
```yaml
name: Hello World Workflow
on:
  workflow_dispatch:

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Print Hello
        run: echo "Hello, world!"

```