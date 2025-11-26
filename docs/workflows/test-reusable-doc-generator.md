# Update Workflow Docs

**Source:** `test-reusable-doc-generator.yml`

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

_None_

## Full YAML
```yaml
name: Update Workflow Docs

on:
  push:
    branches:
      - main
    paths:
      - ".github/workflows/*.yml"
  workflow_dispatch:

jobs:
  generate-docs:
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/generate-workflow-doc.yml@main
    with:
      workflow_dir: ".github/workflows"
      output_dir: "docs/workflows"
      branch_name: "auto-doc/update-workflow-readmes"
      base_branch: "main"

```