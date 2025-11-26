# Mega Jira Workflow

**Source:** `test-jira-main-flow-v2.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### create

_None_

### assign

_None_

## Full YAML
```yaml
name: Mega Jira Workflow

on:
  workflow_dispatch:
    inputs:
      project_key:
        description: "Jira project key (example: ERP)"
        required: true
        type: string
      summary:
        description: "Summary for the Jira ticket"
        required: true
        type: string
      description:
        description: "Description text"
        required: false
        type: string
      assignee_email:
        description: "Email of assignee"
        required: true
        type: string

jobs:
  create:
    name: Create Jira Issue
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/create-jira-issue.yml@main
    with:
      project_key: ${{ inputs.project_key }}
      summary: ${{ inputs.summary }}
      desc: ${{ inputs.description }}
    secrets:
      JIRA_EMAIL: ${{ secrets.JIRA_USER }}
      JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
      JIRA_URL: ${{ secrets.JIRA_BASE_URL }}

  assign:
    name: Assign Jira Issue
    needs: create
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/assign-jira-ticket.yml@main
    with:
      issue_key: ${{ needs.create.outputs.issue_key }}
      assignee_email: ${{ inputs.assignee_email }}
    secrets:
      JIRA_EMAIL: ${{ secrets.JIRA_USER }}
      JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
      JIRA_URL: ${{ secrets.JIRA_BASE_URL }}

```