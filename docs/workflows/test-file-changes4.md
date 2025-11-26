# 🧪 Test File Change Detection

**Source:** `test-file-changes4.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### run-test

_None_

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
 # push:
  #  branches: [ main ]
 # pull_request:
  #  branches: [ main ]
 # release:
  #  types: [published]
   workflow_dispatch:

permissions:
  contents: read

jobs:
  run-test:
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/check-for-file-changes.yml@main
    with:
      watched_files: |
        src/App.java
      current_tag: HEAD
      previous_tag: HEAD~1
  
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