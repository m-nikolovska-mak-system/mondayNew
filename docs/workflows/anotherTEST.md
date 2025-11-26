# 🔍 Test File Watcher

**Source:** `anotherTEST.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### test

_None_

## Full YAML
```yaml
name: 🔍 Test File Watcher

on:
  workflow_dispatch:   

jobs:
  test:
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/check-for-files-changed-v2.yml@main
    with:
      watched_files: |
        .github/workflows/**
        src/**
      # optionally override tags if you want to simulate specific ones
      current_tag:  v1.4.1 
      previous_tag: v1.4.0

```