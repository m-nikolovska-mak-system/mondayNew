# Test Tag Push

**Source:** `tag-test.yml`

## Triggers
- `push`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### print-tag

| name | action | run |
| --- | --- | --- |
| Show pushed tag |  | `run` command |

## Full YAML
```yaml
name: Test Tag Push

on:
  push:
    tags:
      - '*'  

jobs:
  print-tag:
    runs-on: ubuntu-latest
    steps:
      - name: Show pushed tag
        run: |
          echo "Tag pushed: ${{ github.event.ref }}"

```