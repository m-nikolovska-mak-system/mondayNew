🚀 GitHub Actions CI/CD for Java App + Inno Setup Installer
This repository uses GitHub Actions reusable workflows to build a Java application, detect an Inno Setup script, create a Windows installer, and publish it to a GitHub Release.

✅ Overview of Workflow Architecture
Main Workflow: main-build-and-release.yml

Trigger: Runs when a new GitHub Release is created.
Purpose: Orchestrates the entire build and release process by calling reusable workflows.
Jobs:

build_jar → Builds the JAR file and outputs a cache key.
detect_iss → Detects .iss setup script for Inno Setup.
build_installer → Creates a Windows installer using Inno Setup.
upload_release → Downloads the installer artifact and attaches it to the GitHub Release.




✅ Reusable Workflows


build-jar.yml

Builds the Java JAR using Gradle.
Outputs jar_cache_key for caching.



detect-setup-script.yml

Detects .iss setup script in the repo.
Outputs setup_script for installer build.



build-installer.yml

Runs on windows-latest.
Installs Inno Setup via Chocolatey.
Builds the installer .exe using the detected script.
Uploads the installer as an artifact (setup-installer).
Outputs installer_file (full path to .exe).



upload-release.yml

Downloads the installer artifact.
Verifies the file exists.
Uploads the .exe to the GitHub Release using softprops/action-gh-release.




✅ Main Workflow Example
name: Main Build and Release

on:
  release:
    types: [created]

jobs:
  build_jar:
    uses: ./.github/workflows/build-jar.yml
    with:
      release_tag: ${{ github.event.release.tag_name }}

  detect_iss:
    uses: ./.github/workflows/detect-setup-script.yml

  build_installer:
    needs: [build_jar, detect_iss]
    uses: ./.github/workflows/build-installer.yml
    with:
      jar_cache_key: ${{ needs.build_jar.outputs.jar_cache_key }}
      release_tag: ${{ github.event.release.tag_name }}
      setup_script: ${{ needs.detect_iss.outputs.setup_script }}
      app_name: ${{ github.event.repository.name }}
      app_version: ${{ github.event.release.tag_name }}
      output_name: "Setup-${{ github.event.release.tag_name }}"

  upload_release:
    needs: build_installer
    uses: ./.github/workflows/upload-release.yml
    with:
      artifact_path: ${{ needs.build_installer.outputs.installer_file }}
      tag_name: ${{ github.event.release.tag_name }}



✅ Upload Release Workflow Example
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
          if [ ! -f "${{ inputs.artifact_path }}" ]; then
            echo "❌ Installer not found at ${{ inputs.artifact_path }}"
            echo "Files in release-assets:"
            ls -lh ./release-assets
            exit 1
          fi
          echo "✓ Found installer: ${{ inputs.artifact_path }}"

      - name: Upload to GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: ${{ inputs.artifact_path }}
          tag_name: ${{ inputs.tag_name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
 

✅ Workflow Flow Diagram
Release Created
      ↓
[build_jar] → outputs jar_cache_key
      ↓
[detect_iss] → outputs setup_script
      ↓
[build_installer] → builds .exe, uploads artifact, outputs installer_file
      ↓
[upload_release] → downloads artifact, uploads to GitHub Release
