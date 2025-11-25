# 📝 Main Build and Release Workflow

## Overview

**Workflow Name:** `Main Build and Release`

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
5. **Build JAR with Gradle**
   - Runs: `./gradlew jar --no-daemon...`
6. **Validate JAR**
   - Runs: `jar_file=$(ls build/libs/*.jar 2>/dev/null | head -n 1)...`
7. **Generate cache key**
   - Runs: `echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >>...`
8. **Cache built JAR**
   - Uses: `actions/cache/save@v3`

### `detect-setup-script`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Checkout code**
   - Uses: `actions/checkout@v4`
2. **Detect setup script**
   - Runs: `file=$(ls *.iss 2>/dev/null | head -n 1)...`

### `call-installer`

### `upload-to-release`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Download installer artifact**
   - Uses: `actions/download-artifact@v4`
2. **Verify installer exists**
   - Runs: `echo "=== Files downloaded ==="...`
3. **Upload installer to GitHub Release**
   - Uses: `softprops/action-gh-release@v2`

### `notify-on-failure`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Report failure**
   - Runs: `echo "❌ Workflow failed"...`

---

*This documentation is auto-generated. Do not edit manually.*
