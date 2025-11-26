# mainn.yml

**Source:** `mainn.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### hello_world_job

| name | action | run |
| --- | --- | --- |
| actions/checkout@v5 | actions/checkout@v5 |  |
| m-nikolovska-mak-system/composite-actions@main | m-nikolovska-mak-system/composite-actions@main |  |
| Run command |  | `run` command |

## Full YAML
```yaml
on: 
#[push]
  workflow_dispatch: 

jobs:
  hello_world_job:
    runs-on: ubuntu-latest
    name: A job to say hello
    steps:
      - uses: actions/checkout@v5
      - id: foo
        uses: m-nikolovska-mak-system/composite-actions@main
        with:
          who-to-greet: 'Mona the Octocat'
      - run: echo random-number "$RANDOM_NUMBER"
        shell: bash
        env:
          RANDOM_NUMBER: ${{ steps.foo.outputs.random-number }}

```