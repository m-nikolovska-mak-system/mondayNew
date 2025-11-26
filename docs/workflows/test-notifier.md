# Test Teams Notifier

**Source:** `test-notifier.yml`

## Triggers
- `push`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### notify

_None_

## Full YAML
```yaml
name: Test Teams Notifier
on:
  push:
    branches: [ main ]

jobs:
  notify:
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main
    with:
      notification_title: "📢 Deployment Completed!"
      action_required_message: "✅ No action required"
      card_color: "Good"
      files: "index.html, styles.css"
    secrets:
      teams_webhook_url: ${{ secrets.TEAMS_WEBHOOK_URL }}

```