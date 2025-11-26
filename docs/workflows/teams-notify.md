# Teams Notification

**Source:** `teams-notify.yml`

## Triggers
- `push`
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### notify

| name | action | run |
| --- | --- | --- |
| Send simple Teams message |  | `run` command |

## Full YAML
```yaml
name: Teams Notification

on: [push, workflow_dispatch]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Send simple Teams message
        run: |
          echo "📤 Sending notification to Teams..."
          
          # Check if webhook is set
          if [ -z "${{ secrets.TEAMS_WEBHOOK_URL }}" ]; then
            echo "❌ TEAMS_WEBHOOK_URL is not set!"
            exit 1
          fi
          
          # Simple message
          message='{"text":"✅ Hello from GitHub Actions!"}'
          
          # Send to Teams
          response=$(curl -s -o /dev/null -w "%{http_code}" \
            -H "Content-Type: application/json" \
            -d "$message" \
            "${{ secrets.TEAMS_WEBHOOK_URL }}")
          
          echo "HTTP Status: $response"
          
          if [ "$response" = "200" ]; then
            echo "✅ Message sent successfully!"
          else
            echo "❌ Failed to send message (HTTP $response)"
            exit 1
          fi
```