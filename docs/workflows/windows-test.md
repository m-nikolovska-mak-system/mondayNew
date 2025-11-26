# Windows Test Workflow

**Source:** `windows-test.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### test-windows

| name | action | run |
| --- | --- | --- |
| Print system info |  | `run` command |

## Full YAML
```yaml
name: Windows Test Workflow

on:
  workflow_dispatch:

jobs:
  test-windows:
    runs-on: windows-latest
    steps:
      - name: Print system info
        shell: cmd
        run: |
          echo Running on Windows
          ver
          dir
```