# Hello World Workflow

**Source:** `hello.yml`

## Triggers
- `push`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### say-hello

| name | action | run |
| --- | --- | --- |
| Checkout code | actions/checkout@v3 |  |
| Say Hello |  | `run` command |

## Full YAML
```yaml
name: Hello World Workflow

on: push

jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Say Hello
        run: echo "👋 Hello from GitHub Actions!"

```