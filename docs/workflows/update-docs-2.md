# Update Docs for Workflows

**Source:** `update-docs-2.yml`

## Triggers
- `push`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### update-docs

| name | action | run |
| --- | --- | --- |
| actions/checkout@v4 | actions/checkout@v4 |  |
| Generate docs for main action | tj-actions/auto-doc@v3 |  |
| Generate docs for reusable workflow | tj-actions/auto-doc@v3 |  |

## Full YAML
```yaml
name: Update Docs for Workflows
on:
  push:
    branches: [main]

jobs:
  update-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate docs for main action
        uses: tj-actions/auto-doc@v3
        with:
          filename: action.yml
          output: README.md

      - name: Generate docs for reusable workflow
        uses: tj-actions/auto-doc@v3
        with:
          filename: .github/workflows/notify-app-changes-v3.yml
          output: docs/reusable.md

```