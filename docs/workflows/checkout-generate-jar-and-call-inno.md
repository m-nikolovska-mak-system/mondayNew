# Build JAR on Release

**Source:** `checkout-generate-jar-and-call-inno.yml`

## Triggers
- `workflow_dispatch`

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### build

| name | action | run |
| --- | --- | --- |
| Checkout code at release tag | actions/checkout@v4 |  |
| Set up Java | actions/setup-java@v3 |  |
| Make Gradle executable |  | `run` command |
| Build JAR with Gradle |  | `run` command |
| Set cache key |  | `run` command |
| Cache JAR file | actions/cache@v3 |  |
| Install Inno Setup |  | `run` command |
| Build setup.exe with Inno Setup |  | `run` command |
| Upload setup.exe as artifact | actions/upload-artifact@v4 |  |
| List JAR files |  | `run` command |

## Full YAML
```yaml
name: Build JAR on Release

on:
  workflow_dispatch:
    inputs:
      ref:
        description: 'Branch or tag to build'
        required: false
        default: 'main'
#  release:
 #   types: [created]

jobs:
  build:
    runs-on: windows-latest
    
    steps:
      - name: Checkout code at release tag
        uses: actions/checkout@v4
        with:
          ref: ${{ github.event.release.tag_name }}

      - name: Set up Java
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Make Gradle executable
        run: chmod +x gradlew
        
      - name: Build JAR with Gradle
        run: ./gradlew jar --no-daemon
        
      - name: Set cache key
        id: set-cache-key
        run: echo "cache-key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT
        
      - name: Cache JAR file
        uses: actions/cache@v3
        with:
          path: build/libs/*.jar
          key: ${{ steps.set-cache-key.outputs.cache-key }}

      - name: Install Inno Setup
        run: |
          sudo apt-get update
          sudo apt-get install -y wine
          wget https://jrsoftware.org/download.php/is.exe -O is.exe
          wine is.exe /VERYSILENT /DIR="C:\\Program Files\\Inno Setup"

      - name: Build setup.exe with Inno Setup
        run: |
          wine "C:\\Program Files\\Inno Setup\\ISCC.exe" .github/setup-script.iss
          
      - name: Upload setup.exe as artifact
        uses: actions/upload-artifact@v4
        with:
          name: installer
          path: output/setup.exe

      - name: List JAR files
        run: ls -l build/libs

```