# 📝 Build JAR

**Generated:** 2025-11-27 09:42:49

---

## Overview

**Workflow Name:** `Build JAR`

## Triggers

*No triggers defined*

## 🔨 Jobs

### `build-jar`

**Runner:** `ubuntu-latest`

**Job Outputs:**

- `jar_cache_key`: `${{ steps.cache-key.outputs.key }}`

**Steps:**

1. **Checkout code**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `ref`: `${{ inputs.release_tag }}...`

2. **Set up Java 17**
   - 📦 Action: `actions/setup-java@v3`
   - ⚙️ Config:
     - `distribution`: `temurin...`
     - `java-version`: `17...`

3. **Make Gradle wrapper executable**
   - 💻 Run: `chmod +x gradlew...`

4. **Cache Gradle dependencies**
   - 📦 Action: `actions/cache@v3`
   - ⚙️ Config:
     - `path`: `~/.gradle/caches ~/.gradle/wrapper ...`
     - `key`: `${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle...`
     - `restore-keys`: `${{ runner.os }}-gradle- ...`

5. **Build JAR**
   - 💻 Run: `./gradlew ${{ inputs.gradle_task }} --no-daemon...`

6. **Validate JAR**
   - 💻 Run: `jar_file=$(ls build/libs/*.jar 2>/dev/null | head -n 1)...`

7. **Generate cache key**
   - 💻 Run: `echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >>...`

8. **Cache built JAR**
   - 📦 Action: `actions/cache/save@v3`
   - ⚙️ Config:
     - `path`: `build/libs/*.jar...`
     - `key`: `${{ steps.cache-key.outputs.key }}...`

---

*This documentation is auto-generated. Do not edit manually.*
