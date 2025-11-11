# 🧪 ACT Guide: Introduction & Installation

## 📌 What is ACT?

https://github.com/nektos/act is a tool that allows you to run your GitHub Actions locally using Docker. Instead of pushing commits to GitHub to test your workflows, you can simulate events like `push`, `pull_request`, or `workflow_dispatch` directly on your machine.

## ⚙️ Installation

### 1. Install Docker

ACT uses Docker to simulate GitHub runners. Make sure Docker is installed and running:

- https://www.docker.com/products/docker-desktop/
- `sudo apt install docker.io` 

### 2. Install ACT


#### 🟤 Chocolatey (Windows)

```bash
choco install act-cli
```

#### 🟣 Scoop (Windows)


```bash
scoop install act
```


## 🚀 ACT TL;DR (Quick Start)

##### Run the default workflow:
```bash
act
```
Running `act` without any event name specified will run with event **push**.


##### Run a specific event (e.g., push):
```bash
act push
act pull_request
act workflow_dispatch
``` 
##### To list all workflows for a given event, use `-l/--list`
```bash
act -l pull_request
``` 



##### Run a specific job:
```bash
act push
``` 
##### Run a specific job:
```bash
act -j <job_id>
``` 

### 🏷️ Running Specific Workflows with ACT

By default, `act` will attempt to run **all workflows** in `.github/workflows`.  
You can override this behavior using the `-W` or `--workflows` flag to **limit which workflow(s) to run**.

---

#### 1️⃣ Run all workflows in a directory

```bash
act -W .github/workflows/
```

| Command | Description |
|---------|-------------|
| `act` | Runs all workflows triggered by `push` by default. |
| `act -W .github/workflows/` | Run all workflows in a directory, respecting event triggers. |
| `act -W .github/workflows/file.yml` | Run only a specific workflow file. |
| `act <event> -e <event.json> -W <workflow>` | Run a workflow with a **mock event payload**. |


##### Dry-run mode (no actions executed):
```bash
act -dryrun
``` 


##### Set environment variables:
```bash
act --env-file .env
``` 


##### Set secrets inline:
```bash
act -s MY_SECRET=value123
``` 
##### Load secrets from a file:
```bash
act --secret-file .secrets
``` 
##### List all available actions and jobs:

```bash
act -l
``` 


## 📄 Using Event Files to Simulate GitHub Events

When running workflows locally, there’s **no real GitHub event** happening. ACT needs a **mock event payload** to know why and how to run your workflow. This is done via a **JSON file**.

---

### 🧩 Example: Simulate a Pull Request

#### 1️⃣ Create a workflow file

`.github/workflows/pr-workflow.yml`:

```yaml
name: Test PR Workflow

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  print-info:
    runs-on: ubuntu-latest
    steps:
      - name: Show PR info
        run: |
          echo "PR base branch: ${{ github.event.pull_request.base.ref }}"
          echo "PR head branch: ${{ github.event.pull_request.head.ref }}"
```
If your workflow relies on properties from a pull request (e.g., `${{ github.event.pull_request.head.ref }}` or `${{ github.event.pull_request.base.ref }}`), your JSON should include at least these fields:

```json
{
  "pull_request": {
    "head": {
      "ref": "feature-branch"
    },
    "base": {
      "ref": "main"
    }
  }
}
```

Then run act with:

 ```bash
act pull_request -e .github\test-events\pr-event.json -W .github/workflows/pr-workflow.yml
```

##### You should see output like:

```bash
| Release tag: v1.0.0
| Release name: Release v1.0.0
| Draft? false
| Prerelease? false
| Body: Initial release
```

### 🧩 Example: Simulate a Tag Push

Sometimes workflows are triggered by **tags** (e.g., releases). You can test them locally using ACT with a **JSON event file**.

---

#### 1️⃣ Create a minimal workflow

`.github/workflows/tag-test.yml`:

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

#### 2️⃣ Create a test event JSON

```yaml

.github/test-events/tag-event.json:

{
  "ref": "refs/tags/v1.0.0"
}

```

#### 3️⃣ Run the workflow with ACT

```yaml
act push -e .github\test-events\tag-event.json -W .github/workflows/tag-test.yml
```

##### You should see output like:

```bash
| Tag pushed: refs/tags/v1.0.0
```


### 🔐 Using Secrets with ACT


ACT supports multiple ways to provide secrets `($${{ secrets.SECRET_NAME }})` :

##### Inline:

```Shell
 act -s MY_SECRET=some-valueShow more lines

```

##### From environment variables (secure prompt if not set):

```Shell
 act -s MY_SECRET
```
If MY_SECRET is not set in your environment, ACT will prompt you securely.

##### From a file:
```Shell
 act -secret-file .secrets
```

Example .secrets file:
```Shell

TEAMS_WEBHOOK_URL=https://your-teams-webhook-url
```

#### 🧪 Example: Testing Secrets with ACT

Create a .secrets file:

```Shell
TEAMS_WEBHOOK_URL=https://your-teams-webhook-urlShow
```


Example workflow `(.github/workflows/teams-notify.yml)`:

``` yml

name: Teams Notification

on: [push, workflow_dispatch]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Send simple Teams message
        run: |
          echo "📤 Sending notification to Teams..."

          if [ -z "${{ secrets.TEAMS_WEBHOOK_URL }}" ]; then
            echo "❌ TEAMS_WEBHOOK_URL is not set!"
            exit 1
          fi

          message='{"text":"✅ Hello from GitHub Actions!"}'

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


Run the workflow:
```Shell
act workflow_dispatch -W .github/workflows/teams-notify.yml --secret-file .secrets
```

#### 🧪 Example: Run a workflow with inputs from a file

``` bash
act workflow_dispatch --input-file my.input -W .github/workflows/test3.yml
```


#### 🧪 Testing a Reusable Workflow with ACT
This example shows how to manually trigger a reusable workflow using workflow_dispatch and test it locally with ACT.

##### Workflow File: .github/workflows/notify-my-changes.yml


``` yaml
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

##### Run it with ACT

``` bash
act workflow_dispatch -W .github/workflows/notify-my-changes.yml --secret-file .secrets
```







