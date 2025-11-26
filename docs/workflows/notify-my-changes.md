# Notify My Changes

**Source:** `notify-my-changes.yml`

## Triggers
- `workflow_dispatch`

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
name: Notify My Changes

on:
  workflow_dispatch:

jobs:
  notify:
    uses: ./.github/workflows/teams-notify-template.yml
    with:
      notification_title: '🔔 Test Dispatch Run'
      action_required_message: '✅ If you see this in Teams, secrets work!'
      card_color: 'Good'
    secrets:
      teams_webhook_url: ${{ secrets.teams_webhook_url }}

```