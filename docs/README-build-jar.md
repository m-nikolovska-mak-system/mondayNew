# 📝 Reusable Workflow Documentation Template

This file is used as a base template when generating documentation for reusable workflows.

---

## Overview

This document provides usage instructions, inputs, outputs, and behavior for the selected workflow.

---

## Usage

(Add auto-generated documentation below. Do not modify this section manually.)

---

## Notes

* This README is auto-generated based on the workflow file.
* Any changes below the **Usage** section may be overwritten automatically.
* The header and sections above “Usage” remain intact.

---

### Why this template works

✔ Has a **Usage** header — required for your `sed` to insert text under it.
✔ Leaves clean room for auto-doc to inject its tables.
✔ Minimal enough not to conflict with auto-generated content.
✔ Works for all your workflows (ci-build, ci-upload, ci-install, etc.).

---

# Build JAR
**Source:** `build-jar.yml`

## Triggers
- `workflow_call`

## Inputs
| name | type | required | default | description |
| --- | --- | --- | --- | --- |
| release_tag | string | no | main |  |
| gradle_task | string | no | jar |  |

## Outputs
| name | description |
| --- | --- |
| jar_cache_key | Cache key for restored JAR testing hello |

## Secrets
_None_

## Jobs

### build-jar
| name | action | run |
| --- | --- | --- |
| Checkout code | actions/checkout@v4 |  |
| Set up Java 17 | actions/setup-java@v3 |  |
| Make Gradle wrapper executable |  | `run` command |
| Cache Gradle dependencies | actions/cache@v3 |  |
| Build JAR |  | `run` command |
| Validate JAR |  | `run` command |
| Generate cache key |  | `run` command |
| Cache built JAR | actions/cache/save@v3 |  |

## Full YAML
```yaml
name: Build JAR

on:
  workflow_call:
    inputs:
      release_tag:
        required: false
        type: string
        default: "main"
      gradle_task:
        required: false
        type: string
        default: "jar"
    outputs:
      jar_cache_key:
        description: "Cache key for restored JAR testing hello"
        value: ${{ jobs.build-jar.outputs.jar_cache_key }}

      

jobs:
  build-jar:
    runs-on: ubuntu-latest
    outputs:
      jar_cache_key: ${{ steps.cache-key.outputs.key }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          ref: ${{ inputs.release_tag }}

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

      - name: Build JAR
        run: ./gradlew ${{ inputs.gradle_task }} --no-daemon

      - name: Validate JAR
        run: |
          jar_file=$(ls build/libs/*.jar 2>/dev/null | head -n 1)
          if [ -z "$jar_file" ]; then
            echo "❌ No JAR files found"
            exit 1
          fi
          echo "✓ Found $(basename "$jar_file")"

      - name: Generate cache key
        id: cache-key
        run: echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT

      - name: Cache built JAR
        uses: actions/cache/save@v3
        with:
          path: build/libs/*.jar
          key: ${{ steps.cache-key.outputs.key }}
```
