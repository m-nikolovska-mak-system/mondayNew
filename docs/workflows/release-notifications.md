# Release Notifications

**Source:** `release-notifications.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### notify-important-changes

_None_

## Full YAML
```yaml
name: Release Notifications

on:
  # release:
    # types: [published]
 # push:
  #  tags:
   #   - 'v*'
   workflow_dispatch:

jobs:
  notify-important-changes:
    uses: m-nikolovska-mak-system/reusable-workflows/.github/workflows/notify-on-release.yml@main
    with:
      # Get the previous tag for comparison
      base-tag: ${{ github.event.release.target_commitish || 'main' }}
      
      # Customize these patterns for your project!
      file-patterns: |
        app\.java
        src/main/.*\.java
        database/migrations/.*
        config/production\.yml
      
      notification-title: '🚀 Release ${{ github.ref_name }} - Critical Files Changed'
    secrets:
      TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}

```