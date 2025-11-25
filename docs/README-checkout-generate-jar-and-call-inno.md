<div align="center">

# 🚀 Build JAR on Release

![Auto-generated](https://img.shields.io/badge/docs-auto--generated-blue?style=flat-square)
![Workflow](https://img.shields.io/badge/type-github--workflow-purple?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2025.11.25-green?style=flat-square)

</div>

---

## 📋 Overview

> **Workflow File:** `.github/workflows/checkout-generate-jar-and-call-inno.yml`

## ⚡ Triggers

<table>
<tr><th>Event</th><th>Details</th></tr>
<tr><td colspan='2'><em>No triggers defined</em></td></tr>
</table>

## 🔨 Jobs

### 🎯 `build`

**🖥️ Runner:** `windows-latest`

<details>
<summary>📝 Steps</summary>

#### 1. Checkout code at release tag

```yaml
uses: actions/checkout@v4
with:
  ref: ${{ github.event.release.tag_name }}
```

#### 2. Set up Java

```yaml
uses: actions/setup-java@v3
with:
  distribution: temurin
  java-version: 17
```

#### 3. Make Gradle executable

```bash
chmod +x gradlew
```

#### 4. Build JAR with Gradle

```bash
./gradlew jar --no-daemon
```

#### 5. Set cache key

```bash
echo "cache-key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT
```

#### 6. Cache JAR file

```yaml
uses: actions/cache@v3
with:
  path: build/libs/*.jar
  key: ${{ steps.set-cache-key.outputs.cache-key }}
```

#### 7. Install Inno Setup

```bash
sudo apt-get update
sudo apt-get install -y wine
wget https://jrsoftware.org/download.php/is.exe -O is.exe
wine is.exe /VERYSILENT /DIR="C:\\Program Files\\Inno Setup"
```

#### 8. Build setup.exe with Inno Setup

```bash
wine "C:\\Program Files\\Inno Setup\\ISCC.exe" .github/setup-script.iss
```

#### 9. Upload setup.exe as artifact

```yaml
uses: actions/upload-artifact@v4
with:
  name: installer
  path: output/setup.exe
```

#### 10. List JAR files

```bash
ls -l build/libs
```

</details>

---

<div align="center">

**📅 Last Updated:** November 25, 2025 at 10:01 UTC

*Auto-generated documentation. Manual edits will be overwritten.*

</div>
