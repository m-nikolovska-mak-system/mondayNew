<div align="center">

# 🚀 Main Build and Release

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/main-build.yml`

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
jar_cache_key: ${{ steps.cache-key.outputs.key }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ github.event.release.tag_name || 'main' }}
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
./gradlew jar --no-daemon
```

#### 6. Validate JAR

```bash
jar_file=$(ls build/libs/*.jar 2>/dev/null | head -n 1)
if [ -z "$jar_file" ]; then
  echo "❌ No JAR files found"
  exit 1
fi
# ... (truncated)
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

### 🎯 `detect-setup-script`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📊 Job Outputs</summary>

```yaml
setup_script: ${{ steps.detect-iss.outputs.script }}
```

</details>

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code

```yaml
uses: actions/checkout@v4
```

#### 2. Detect setup script

```bash
file=$(ls *.iss 2>/dev/null | head -n 1)
if [ -z "$file" ]; then
  echo "❌ No .iss setup script found!"
  exit 1
fi
# ... (truncated)
```

</details>

### 🎯 `call-installer`

**📞 Calls:** `m-nikolovska-mak-system/reusable-actions-library/.github/workflows/build-installer.yml@main`

### 🎯 `upload-to-release`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Download installer artifact

```yaml
uses: actions/download-artifact@v4
with:
  name: setup-installer
  path: output
```

#### 2. Verify installer exists

```bash
echo "=== Files downloaded ==="
ls -lh output/

expected="Setup-${{ github.event.release.tag_name }}.exe"
if [ ! -f "output/$expected" ]; then
# ... (truncated)
```

#### 3. Upload installer to GitHub Release

```yaml
uses: softprops/action-gh-release@v2
with:
  files: output/*.exe
  tag_name: ${{ github.event.release.tag_name }}
```

</details>

### 🎯 `notify-on-failure`

**🖥️ Runner:** `ubuntu-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Report failure

```bash
echo "❌ Workflow failed"
echo "Failed jobs: ${{ toJSON(needs) }}"
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
