# 📝 Build JAR on Release Workflow

## Overview

**Workflow Name:** `Build JAR on Release`

## Triggers


## Jobs

### `build`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code at release tag**
   - Uses: `actions/checkout@v4`
2. **Set up Java**
   - Uses: `actions/setup-java@v3`
3. **Make Gradle executable**
   - Runs: `chmod +x gradlew...`
4. **Build JAR with Gradle**
   - Runs: `./gradlew jar --no-daemon...`
5. **Set cache key**
   - Runs: `echo "cache-key=jar-${{ github.sha }}-${{ github.run_number ...`
6. **Cache JAR file**
   - Uses: `actions/cache@v3`
7. **Upload JAR as artifact**
   - Uses: `actions/upload-artifact@v3`
8. **List JAR files**
   - Runs: `ls -l build/libs...`

---

*This documentation is auto-generated. Do not edit manually.*
