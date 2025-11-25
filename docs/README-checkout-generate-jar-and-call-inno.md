# 📝 Build JAR on Release Workflow

## Overview

**Workflow Name:** `Build JAR on Release`

## Triggers


## Jobs

### `build`

**Runner:** `windows-latest`

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
7. **Install Inno Setup**
   - Runs: `sudo apt-get update...`
8. **Build setup.exe with Inno Setup**
   - Runs: `wine "C:\\Program Files\\Inno Setup\\ISCC.exe" .github/setup...`
9. **Upload setup.exe as artifact**
   - Uses: `actions/upload-artifact@v4`
10. **List JAR files**
   - Runs: `ls -l build/libs...`

---

*This documentation is auto-generated. Do not edit manually.*
