# 📝 Build JAR Workflow

## Overview

**Workflow Name:** `Build JAR`

## Triggers


## Jobs

### `build-jar`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Set up Java 17**
   - Uses: `actions/setup-java@v3`
3. **Make Gradle wrapper executable**
   - Runs: `chmod +x gradlew...`
4. **Cache Gradle dependencies**
   - Uses: `actions/cache@v3`
5. **Build JAR**
   - Runs: `./gradlew ${{ inputs.gradle_task }} --no-daemon...`
6. **Validate JAR**
   - Runs: `jar_file=$(ls build/libs/*.jar 2>/dev/null | head -n 1)...`
7. **Generate cache key**
   - Runs: `echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >>...`
8. **Cache built JAR**
   - Uses: `actions/cache/save@v3`

---

*This documentation is auto-generated. Do not edit manually.*
