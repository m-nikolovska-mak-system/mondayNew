# Generate Workflow Docs

**Source:** `generate-workflow-docs.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### build-doc

| name | action | run |
| --- | --- | --- |
| actions/checkout@v4 | actions/checkout@v4 |  |
| Ensure output directory exists |  | `run` command |
| Generate README with auto-doc | tj-actions/auto-doc@v3 |  |
| Debug git status |  | `run` command |
| Commit generated docs | EndBug/add-and-commit@v9 |  |

## Full YAML
```yaml

name: Generate Workflow Docs

on:
  workflow_dispatch:
    inputs:
      filename:
        description: 'Path to the workflow or action file'
        required: true
        default: .github/workflows/hello.yml
      output:
        description: 'Output markdown path'
        required: false
        default: docs/workflow-docs.md

jobs:
  build-doc:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name:  Ensure output directory exists
        run: mkdir -p $(dirname "${{ github.event.inputs.output }}")
      
      - name: Generate README with auto-doc
        uses: tj-actions/auto-doc@v3
        with:
          filename: ${{ github.event.inputs.filename }}
          output: ${{ github.event.inputs.output }}
      
      - name: Debug git status
        run: git status --short
      
      - name: Commit generated docs
        uses: EndBug/add-and-commit@v9
        with:
          author_name: github-actions[bot]
          author_email: 41898282+github-actions[bot]@users.noreply.github.com
          message: "chore(docs): update workflow docs"
          add: '.'
          push: true
          allow_empty_commit: true

```