# Upload Release Artifact

**Source:** `upload-release.yml`

## Triggers
- `workflow_call`

## Inputs
| name | type | required | default | description |
| --- | --- | --- | --- | --- |
| tag_name | string | yes |  |  |
| artifact_path | string | yes |  |  |

## Outputs
_None_

## Secrets
_None_

## Jobs
### upload

| name | action | run |
| --- | --- | --- |
| Download installer artifact | actions/download-artifact@v4 |  |
| Verify artifact exists |  | `run` command |
| Upload to GitHub Release | softprops/action-gh-release@v2 |  |

## Full YAML
```yaml
name: Upload Release Artifact

on:
  workflow_call:
    inputs:
      tag_name:
        required: true
        type: string
      artifact_path:
        required: true
        type: string

        

jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Download installer artifact
        uses: actions/download-artifact@v4
        with:
          name: setup-installer
          path: ./release-assets

      - name: Verify artifact exists
        run: |
          echo "=== Files in release-assets ==="
          ls -lh ./release-assets/
          
          files=$(ls ./release-assets/*.exe 2>/dev/null)
          if [ -z "$files" ]; then
            echo "❌ No installer files found in ./release-assets"
            exit 1
          fi
          echo "✓ Found installer files: $files"

            
      - name: Upload to GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: ./release-assets/*.exe  
          tag_name: ${{ inputs.tag_name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}


```