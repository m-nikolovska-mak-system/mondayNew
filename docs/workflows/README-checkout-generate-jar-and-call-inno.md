# 📝 Build JAR on Release

**Generated:** 2025-11-25 14:14:13 UTC

---

## Overview

**Workflow File:** `.github/workflows/checkout-generate-jar-and-call-inno.yml`

## ⚡ Triggers

| Event | Details |
|-------|---------|
| – | No triggers defined |

## 🔨 Jobs

### `build`

**Runner:** `windows-latest`

**Steps:**

1. **Checkout code at release tag**
   - 📦 Action: `actions/checkout@v4`
   - ⚙️ Config:
     - `ref`: `${{ github.event.release.tag_name }}`

2. **Set up Java**
   - 📦 Action: `actions/setup-java@v3`
   - ⚙️ Config:
     - `distribution`: `temurin`
     - `java-version`: `17`

3. **Make Gradle executable**
   - 💻 Run: `chmod +x gradlew...`

4. **Build JAR with Gradle**
   - 💻 Run: `./gradlew jar --no-daemon...`

5. **Set cache key**
   - 💻 Run: `echo "cache-key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT...`

6. **Cache JAR file**
   - 📦 Action: `actions/cache@v3`
   - ⚙️ Config:
     - `path`: `build/libs/*.jar`
     - `key`: `${{ steps.set-cache-key.outputs.cache-key }}`

7. **Install Inno Setup**
   - 💻 Run: `sudo apt-get update sudo apt-get install -y wine wget https://jrsoftware.org/download.php/is.exe -O is.exe wine is.exe /...`

8. **Build setup.exe with Inno Setup**
   - 💻 Run: `wine "C:\\Program Files\\Inno Setup\\ISCC.exe" .github/setup-script.iss...`

9. **Upload setup.exe as artifact**
   - 📦 Action: `actions/upload-artifact@v4`
   - ⚙️ Config:
     - `name`: `installer`
     - `path`: `output/setup.exe`

10. **List JAR files**
   - 💻 Run: `ls -l build/libs...`

---

*This documentation is auto-generated. Do not edit manually.*
