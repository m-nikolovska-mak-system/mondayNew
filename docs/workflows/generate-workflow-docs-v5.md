# Generate Workflow Documentation

**Source:** `generate-workflow-docs-v5.yml`

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
### generate-docs

| name | action | run |
| --- | --- | --- |
| actions/checkout@v4 | actions/checkout@v4 |  |
| Setup Node | actions/setup-node@v4 |  |
| Install dependencies |  | `run` command |
| Generate workflow docs |  | `run` command |
| Create Pull Request for updated workflow docs | peter-evans/create-pull-request@v6 |  |

## Full YAML
```yaml
name: Generate Workflow Documentation

on:
  push:
    branches:
      - main
    paths:
      - ".github/workflows/*.yml"
      - ".github/workflows/*.yaml"
  workflow_dispatch:

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm install

      - name: Generate workflow docs
        run: node scripts/generate-workflow-docs.js

      - name: Create Pull Request for updated workflow docs
        uses: peter-evans/create-pull-request@v6
        with:
          commit-message: "docs: auto-update workflow READMEs"
          title: "docs: auto-update workflow READMEs"
          body: "This PR updates the documentation for workflows in .github/workflows."
          branch: "auto-doc/update-workflow-readmes"
          base: main
          token: ${{ secrets.GITHUB_TOKEN }}

```