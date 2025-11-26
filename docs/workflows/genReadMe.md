# Generate README

**Source:** `genReadMe.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### generate-readme

| name | action | run |
| --- | --- | --- |
| actions/checkout@v3 | actions/checkout@v3 |  |
| Generate README | bitflight-devops/github-action-readme-generator@v1 |  |

## Full YAML
```yaml
name: Generate README
on:
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate README
        uses: bitflight-devops/github-action-readme-generator@v1
        with:
          action: .github/workflows/hello.yml
          readme: AUTO_README.md
          save: false

```