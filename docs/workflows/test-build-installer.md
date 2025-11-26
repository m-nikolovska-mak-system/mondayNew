# Test Build Installer

**Source:** `test-build-installer.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### test_build_installer

_None_

## Full YAML
```yaml
name: Test Build Installer
on:
  workflow_dispatch:

jobs:
  test_build_installer:
    uses: ./.github/workflows/build-installer.yml
    with:
      jar_cache_key: "mock-key"
      release_tag: "v1.0.0"
      setup_script: "setup-script.iss"
      app_name: "MyApp"
      app_version: "1.0.0"
      output_name: "Setup-v1.0.0"

```