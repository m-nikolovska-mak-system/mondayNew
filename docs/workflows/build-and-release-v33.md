# Build & Release Java App version 3

**Source:** `build-and-release-v33.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### build_jar

_None_

### detect_iss

_None_

### validate_inputs

| name | action | run |
| --- | --- | --- |
| Check jar_cache_key |  | `run` command |

### build_installer

_None_

### upload_release

_None_

### notify_success

_None_

### notify_failure

_None_

## Full YAML
```yaml
name: Build & Release Java App version 3

on:
  workflow_dispatch:
    inputs:
      java_version:
        description: 'Java version'
        required: false
        default: '17'
      java_distribution:
        description: 'Java distribution'
        required: false
        default: 'temurin'
      gradle_task:
        description: 'Gradle task to run'
        required: false
        default: 'jar'
#  release:
 #   types: [created]

concurrency:
  group: ${{ github.workflow }}-${{ github.event.release.tag_name || github.run_id }}
  cancel-in-progress: false

jobs:
  build_jar:
    name: Build JAR
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-jar.yml@main
    with:
      release_tag: ${{ github.event.release.tag_name }}
      gradle_task: ${{ inputs.gradle_task || 'jar' }}
      java_version: ${{ inputs.java_version || '17' }}
      java_distribution: ${{ inputs.java_distribution || 'temurin' }}

  detect_iss:
    name: Detect Setup Script
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/detect-setup-script.yml@main
    with:
      pattern: "**/*.iss"
      fail_if_missing: true

  validate_inputs:
    name: Validate JAR cache key
    needs: build_jar
    runs-on: ubuntu-latest
    steps:
      - name: Check jar_cache_key
        run: |
          if [ -z "${{ needs.build_jar.outputs.jar_cache_key }}" ]; then
            echo "::error::JAR cache key is empty!"
            exit 1
          fi

  build_installer:
    name: Build Windows Installer
    needs: [build_jar, detect_iss, validate_inputs]
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main
    with:
      setup_script: ${{ needs.detect_iss.outputs.setup_script }}
      jar_path: ${{ needs.build_jar.outputs.jar_path }}
      jar_cache_key: ${{ needs.build_jar.outputs.jar_cache_key }}
      app_name: ${{ github.event.repository.name }}
      app_version: ${{ github.event.release.tag_name }}
      output_name: "Setup-${{ github.event.release.tag_name }}"

  upload_release:
    name: Upload Release Asset
    needs: build_installer
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/upload-release.yml@main
    with:
      tag_name: ${{ github.event.release.tag_name }}
      artifact_name: ${{ needs.build_installer.outputs.installer_artifact_name }}

  notify_success:
    name: Notify Success
    if: success() && github.event_name == 'release'
    needs: [build_jar, detect_iss, validate_inputs, build_installer, upload_release]
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main
    with:
      notification_title: "✅ Build & Release Succeeded!"
      action_required_message: "Release ${{ github.event.release.tag_name }} is ready. View: ${{ github.event.release.html_url }}"
    secrets:
      teams_webhook_url: ${{ secrets.TEAMS_WEBHOOK_URL }}

  notify_failure:
    name: Notify Failure
    if: failure()
    needs: [build_jar, detect_iss, validate_inputs, build_installer, upload_release]
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/teams-notifier.yml@main
    with:
      notification_title: "🚨 Build & Release Failed!"
      action_required_message: "Check logs: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"
    secrets:
      teams_webhook_url: ${{ secrets.TEAMS_WEBHOOK_URL }}

```