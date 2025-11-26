# Checkout on Release

**Source:** `checkout-on-release.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### checkout

| name | action | run |
| --- | --- | --- |
| Checkout code at release tag | actions/checkout@v4 |  |
| Show current commit and tag |  | `run` command |

## Full YAML
```yaml
name: Checkout on Release

on:
#  release:
 #   types: [created]
  workflow_dispatch: 
jobs:
  checkout:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code at release tag
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.release.tag_name }}

      - name: Show current commit and tag
        run: |
          echo "Checked out tag: ${{ github.event.release.tag_name }}"
          git log -1

```