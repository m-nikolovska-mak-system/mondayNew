# Detect Setup Script

**Source:** `detect-setup-script.yml`

## Triggers
- `workflow_call`

## Inputs
_None_

## Outputs
| name | description |
| --- | --- |
| setup_script | Detected .iss setup script |

## Secrets
_None_

## Jobs
### detect-iss

| name | action | run |
| --- | --- | --- |
| Checkout code | actions/checkout@v4 |  |
| Detect .iss setup script |  | `run` command |

## Full YAML
```yaml
name: Detect Setup Script

on:
  workflow_call:
    outputs:
      setup_script:
        description: "Detected .iss setup script"
        value: ${{ jobs.detect-iss.outputs.setup_script }}

jobs:
  detect-iss:
    runs-on: ubuntu-latest
    outputs:
      setup_script: ${{ steps.detect.outputs.script }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Detect .iss setup script
        id: detect
        run: |
          file=$(ls *.iss 2>/dev/null | head -n 1)
          if [ -z "$file" ]; then
            echo "❌ No .iss setup script found!"
            exit 1
          fi
          echo "Found setup script: $file"
          echo "script=$file" >> $GITHUB_OUTPUT

```