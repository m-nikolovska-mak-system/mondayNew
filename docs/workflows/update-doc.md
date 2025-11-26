# Update README with Action Docs

**Source:** `update-doc.yml`

## Triggers
- `push`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### update-doc

| name | action | run |
| --- | --- | --- |
| actions/checkout@v4 | actions/checkout@v4 |  |
| Run auto-doc | tj-actions/auto-doc@v3 |  |

## Full YAML
```yaml
name: Update README with Action Docs
on:
  push:
    branches:
      - main

jobs:
  update-doc:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run auto-doc
        uses: tj-actions/auto-doc@v3
        with:
          filename: action.yml       

```