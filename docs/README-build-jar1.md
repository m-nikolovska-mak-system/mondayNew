<div align="center">

# 🚀 OVA TREBA DA RABOTI Build JAR

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/build-jar1.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build-jar`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
jar-cache-key: ${{ steps.cache-key.outputs.key }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ github.event.release.tag_name || github.event.inputs.ref...
```

#### 2. Set up Java 17

```yaml
uses: actions/setup-java@v3
with:
  distribution: temurin
  java-version: 17
```

#### 3. Make Gradle wrapper executable

```bash
chmod +x gradlew
```

#### 4. Cache Gradle dependencies

```yaml
uses: actions/cache@v3
with:
  path: ~/.gradle/caches ~/.gradle/wrapper 
  key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gr...
  restore-keys: ${{ runner.os }}-gradle- 
```

#### 5. Build JAR with Gradle

```bash
./gradlew clean jar --no-daemon
```

#### 6. Upload JAR as artifact

```yaml
uses: actions/upload-artifact@v4
with:
  name: app-jar
  path: build/libs/*.jar
```

#### 7. Generate cache key

```bash
echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT
```

#### 8. Cache built JAR

```yaml
uses: actions/cache/save@v3
with:
  path: build/libs/*.jar
  key: ${{ steps.cache-key.outputs.key }}
```

</details>

### 🎯 `build-installer`

**🖥️ Runner:** `windows-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout repo

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ github.event.release.tag_name || github.event.inputs.ref...
```

#### 2. Download JAR artifact

```yaml
uses: actions/download-artifact@v4
with:
  name: app-jar
  path: build/libs
```

#### 3. Rename JAR to App.jar

```bash
$jar = Get-ChildItem build\libs\*.jar | Select-Object -First 1
if ($jar.Name -ne "App.jar") {
  Rename-Item $jar.FullName -NewName "App.jar"
}
```

#### 4. Verify JAR

```bash
dir build\libs
```

#### 5. Install Inno Setup

```bash
choco install innosetup --no-progress -y
```

#### 6. Build setup.exe

```bash
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup-script.iss
```

#### 7. Check output folder

```bash
dir output
```

#### 8. Upload setup.exe to GitHub Release

```yaml
uses: softprops/action-gh-release@v2
with:
  files: output/OneProjectWed-Setup.exe
  tag_name: ${{ github.event.release.tag_name }}
```

#### 9. Upload setup.exe as artifact (for workflow_dispatch)

```yaml
uses: actions/upload-artifact@v4
with:
  name: setup-installer
  path: output/OneProjectWed-Setup.exe
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
