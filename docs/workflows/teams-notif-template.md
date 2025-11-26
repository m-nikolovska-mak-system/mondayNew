# Teams Notification Template

**Source:** `teams-notif-template.yml`

## Triggers
- `workflow_call`

## Inputs
| name | type | required | default | description |
| --- | --- | --- | --- | --- |
| notification_title | string | yes |  |  |
| action_required_message | string | no | ⚠️ Reminder: Changes detected that may require action |  |
| card_color | string | no | Accent |  |

## Outputs
_None_

## Secrets
| name | required | description |
| --- | --- | --- |
| teams_webhook_url | yes |  |

## Jobs
### send-notification

| name | action | run |
| --- | --- | --- |
| Checkout repository | actions/checkout@v4 |  |
| Make script executable |  | `run` command |
| Send Microsoft Teams notification |  | `run` command |
| Test failure message |  | `run` command |

## Full YAML
```yaml
name: Teams Notification Template

on:
  workflow_call:
    inputs:
      notification_title:
        required: true
        type: string
      action_required_message:
        required: false
        type: string
        default: '⚠️ Reminder: Changes detected that may require action'
      card_color:
        required: false
        type: string
        default: 'Accent'
    secrets:
      teams_webhook_url:
        required: true

jobs:
  send-notification:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4


      - name: Make script executable
        run: chmod +x ./scripts/send-teams-notification.sh
  
      
      - name: Send Microsoft Teams notification
        env:
          TEAMS_WEBHOOK_URL: ${{ secrets.teams_webhook_url }}
          NOTIFICATION_TITLE: ${{ inputs.notification_title }}
          ACTION_MESSAGE: ${{ inputs.action_required_message }}
          CARD_COLOR: ${{ inputs.card_color }}
        run: ./scripts/send-teams-notification.sh


      - name: Test failure message
        run: echo "This should fail" && false

```