# Generate Action Docs

**Source:** `readme-gen-2.yml`

## Triggers
- `workflow_dispatch`
- `push`

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
| actions/checkout@v3 | actions/checkout@v3 |  |
| Generate docs | nektos/action-docs@v2 |  |

## Full YAML
```yaml
name: Generate Action Docs

on:
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate docs
        uses: nektos/action-docs@v2

```