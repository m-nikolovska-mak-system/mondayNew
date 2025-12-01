# Build JAR this is a duplicate with a differenect name to HELLOO aaaaaaaaaaa testingaaaaaaaaaaa

## 📋 Overview

This document provides comprehensive documentation for the **Build JAR this is a duplicate with a differenect name to HELLOO aaaaaaaaaaa testingaaaaaaaaaaa** workflow.

---

## 🎯 Triggers



---

## 📥 Inputs

_This workflow does not accept any inputs._

---

## 📤 Outputs

_This workflow does not expose any outputs._

---

## 🔐 Secrets

_This workflow does not require any secrets._

---

## 💼 Jobs

### `build-jar`

**Runs on:** `ubuntu-latest`

| Step | Uses | Run Command |
| ---- | ---- | ----------- |
| Checkout code | `actions/checkout@v4` |  |
| Set up Java 17 | `actions/setup-java@v3` |  |
| Make Gradle wrapper executable |  | `chmod +x gradlew` |
| Cache Gradle dependencies | `actions/cache@v3` |  |
| Build JAR |  | `./gradlew ${{ inputs.gradle_task }} --no-daemon` |
| Validate JAR |  | ✅ Yes (see YAML) |
| Generate cache key |  | ✅ Yes (see YAML) |
| Cache built JAR | `actions/cache/save@v3` |  |

---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
name: Build JAR this is a duplicate with a differenect name to HELLOO aaaaaaaaaaa testingaaaaaaaaaaa
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
      gradle_task_two0aao:
        required: false
        type: string
        default: "jar33333"
    outputs:
      jar_cache_key:
        description: "Cache key for restored JARrrrr hello test"
        value: ${{ jobs.build-jar.outputs.jar_cache_key }}
    secrets:
      TEST_SECRETT:
        required: true

      

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

</details>

---

**Generated on:** 2025-12-01 11:30:20
