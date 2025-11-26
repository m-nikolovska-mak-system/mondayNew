# 🧪 Test File Change Detection

**Source:** `test-check-file-changes.yml`

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
### check_changes

_None_

### on_changes

| name | action | run |
| --- | --- | --- |
| ✅ Watched files changed |  | `run` command |

### on_no_changes

| name | action | run |
| --- | --- | --- |
| ℹ️ No relevant changes |  | `run` command |

## Full YAML
```yaml
name: 🧪 Test File Change Detection

on:
  workflow_dispatch:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
 # release:
  #  types: [published]

permissions:
  contents: read

jobs:
  check_changes:
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/check-for-file-changes.yml@main
    with:
      watched_files: |
        src/**
        config/**
        README.md

  on_changes:
    needs: check_changes
    if: needs.check_changes.outputs.files_changed == 'true'
    runs-on: ubuntu-latest
    steps:
      - name: ✅ Watched files changed
        run: |
          echo "Changed files:"
          echo "${{ needs.check_changes.outputs.changed_files_list }}"

  on_no_changes:
    needs: check_changes
    if: needs.check_changes.outputs.files_changed == 'false'
    runs-on: ubuntu-latest
    steps:
      - name: ℹ️ No relevant changes
        run: echo "No watched files changed!"

```