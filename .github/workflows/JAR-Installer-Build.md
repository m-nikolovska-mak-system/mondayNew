# 🚀 GitHub Actions Workflows for JAR & Installer Build
This repository contains **two GitHub Actions workflows** designed to automate the build and release process for a Java application and its Windows installer.

---

## ✅ Overview

We have split the build process into **two workflows**:

1. **Main Build and Release (`main-build.yml`)**  
   - Triggered on **GitHub Release creation** or manually via `workflow_dispatch`.
   - Builds the JAR file using Gradle.
   - Caches the JAR for reuse.
   - Calls the reusable workflow to build the installer.
   - Uploads the final installer (`.exe`) to the GitHub Release.

2. **Build Installer (`build-installer.yml`)**  
   - A **reusable workflow** triggered by `workflow_call`.
   - Restores the cached JAR.
   - Builds the Windows installer using **Inno Setup**.
   - Uploads the installer as an artifact for the calling workflow.

---

## ✅ Workflow Structure

### **1. Main Build and Release (`.github/workflows/main-build.yml`)**

**Purpose:**  
- Acts as the **entry point** for the build process.
- Handles JAR build and release upload.

**Triggers:**  
- `release: created`  
- `workflow_dispatch` (manual trigger)

**Key Steps:**  
- Checkout code.
- Set up Java 17.
- Build JAR with Gradle.
- Cache JAR for later use.
- Call `build-installer.yml` workflow.
- Upload installer to GitHub Release.

```yaml
name: Main Build and Release
on:
  release:
    types: [created]
  workflow_dispatch:
    inputs:
      ref:
        description: 'Branch or tag to build'
        required: false
        default: 'main'

jobs:
  build-jar:
    runs-on: ubuntu-latest
    outputs:
      jar-cache-key: ${{ steps.cache-key.outputs.key }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.release.tag_name || github.event.inputs.ref || 'main' }}

      - name: Set up Java 17
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Make Gradle wrapper executable
        run: chmod +x gradlew

      - name: Cache Gradle dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.gradle/caches
            ~/.gradle/wrapper
          key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}
          restore-keys: |
            ${{ runner.os }}-gradle-

      - name: Build JAR with Gradle
        run: ./gradlew clean jar --no-daemon

      - name: Generate cache key
        id: cache-key
        run: echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT

      - name: Cache built JAR
        uses: actions/cache/save@v3
        with:
          path: build/libs/*.jar
          key: ${{ steps.cache-key.outputs.key }}

  call-installer:
    needs: build-jar
    uses: ./.github/workflows/build-installer.yml
    with:
      jar-cache-key: ${{ needs.build-jar.outputs.jar-cache-key }}

  upload-to-release:
    needs: call-installer
    runs-on: ubuntu-latest
    steps:
      - name: Download installer artifact
        uses: actions/download-artifact@v4
        with:
          name: setup-installer
          path: output

      - name: Upload setup.exe to GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: output/OneProjectWed-Setup.exe
          tag_name: ${{ github.event.release.tag_name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
