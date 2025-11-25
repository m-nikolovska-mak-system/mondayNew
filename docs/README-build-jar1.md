# 📝 OVA TREBA DA RABOTI Build JAR Workflow

## Overview

**Workflow Name:** `OVA TREBA DA RABOTI Build JAR`

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
   - Runs: `./gradlew clean jar --no-daemon...`
6. **Upload JAR as artifact**
   - Uses: `actions/upload-artifact@v4`
7. **Generate cache key**
   - Runs: `echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >>...`
8. **Cache built JAR**
   - Uses: `actions/cache/save@v3`

### `build-installer`

**Runner:** `windows-latest`

**Steps:**

1. **Checkout repo**
   - Uses: `actions/checkout@v4`
2. **Download JAR artifact**
   - Uses: `actions/download-artifact@v4`
3. **Rename JAR to App.jar**
   - Runs: `$jar = Get-ChildItem build\libs\*.jar | Select-Object -First...`
4. **Verify JAR**
   - Runs: `dir build\libs...`
5. **Install Inno Setup**
   - Runs: `choco install innosetup --no-progress -y...`
6. **Build setup.exe**
   - Runs: `& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup-scrip...`
7. **Check output folder**
   - Runs: `dir output...`
8. **Upload setup.exe to GitHub Release**
   - Uses: `softprops/action-gh-release@v2`
9. **Upload setup.exe as artifact (for workflow_dispatch)**
   - Uses: `actions/upload-artifact@v4`

---

*This documentation is auto-generated. Do not edit manually.*
