# Test Teams Notification

**Source:** `test-teams-noti.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### test-notification

_None_

## Full YAML
```yaml
name: Test Teams Notification

on:
  workflow_dispatch:

jobs:
  test-notification:
    uses: ./.github/workflows/teams-notif-template.yml
    with:
      notification_title: "🧪 Test Notification from Act"
      action_required_message: "This is a test message"
      card_color: "Accent"
    secrets:
      teams_webhook_url: ${{ secrets.TEAMS_WEBHOOK_URL }}
```