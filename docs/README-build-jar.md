<div align="center">

# 🚀 Build JAR

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/build-jar.yml`

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
  ref: ${{ inputs.release_tag }}
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

#### 5. Build JAR

```bash
./gradlew ${{ inputs.gradle_task }} --no-daemon
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

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:30 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
