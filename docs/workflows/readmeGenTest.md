# README Info Update

**Source:** `readmeGenTest.yml`

## Triggers
- `schedule`
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### update-readme

| name | action | run |
| --- | --- | --- |
| anmol098/waka-readme-stats@master | anmol098/waka-readme-stats@master |  |

## Full YAML
```yaml
name: README Info Update

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  update-readme:
    name: Update README
    runs-on: ubuntu-latest
    steps:
      - uses: anmol098/waka-readme-stats@master
        with:
          GH_TOKEN: ${{ secrets.GH_PAT }}
          SHOW_LINES_OF_CODE: "True"
          SHOW_PROFILE_VIEWS: "True"
          SHOW_TOTAL_CONTRIBUTIONS: "True"
          TIMEZONE: "Europe/Skopje"

```