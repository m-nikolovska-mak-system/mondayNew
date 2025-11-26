# Build JAR this is a duplicate with a differenect name to test readmethis is a change hi hello hiii hi
**Source:** `ci-build-jar.yml`

## Triggers
_None_

## Inputs
_None_

## Outputs
_None_

## Secrets
_None_

## Jobs
### build-jar

| name | action | run |
| --- | --- | --- |
| Checkout code | actions/checkout@v4 |  |
| Set up Java 17 | actions/setup-java@v3 |  |
| Make Gradle wrapper executable |  | `run` command |
| Cache Gradle dependencies | actions/cache@v3 |  |
| Build JAR |  | `run` command |
| Validate JAR |  | `run` command |
| Generate cache key |  | `run` command |
| Cache built JAR | actions/cache/save@v3 |  |

## Full YAML
```yaml
name: Build JAR this is a duplicate with a differenect name to test readmethis is a change hi hello hiii hi

on:
  workflow_call:
    inputs:
      release_tag:
        required: false
        type: string
        default: "main"
      gradle_task:
        required: false
        type: string
        default: "jar"
    outputs:
      jar_cache_key:
        description: "Cache key for restored JAR"
        value: ${{ jobs.build-jar.outputs.jar_cache_key }}

      

jobs:
  build-jar:
    runs-on: ubuntu-latest
    outputs:
      jar_cache_key: ${{ steps.cache-key.outputs.key }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          ref: ${{ inputs.release_tag }}

      - name: Set up Java 17
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Make Gradle wrapper executable
        run: chmod +x gradlew

      - name: Cache Gradle dependencies
        uses: actions/cache@v3
        with:
          path: |
            ~/.gradle/caches
            ~/.gradle/wrapper
          key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}
          restore-keys: |
            ${{ runner.os }}-gradle-

      - name: Build JAR
        run: ./gradlew ${{ inputs.gradle_task }} --no-daemon

      - name: Validate JAR
        run: |
          jar_file=$(ls build/libs/*.jar 2>/dev/null | head -n 1)
          if [ -z "$jar_file" ]; then
            echo "❌ No JAR files found"
            exit 1
          fi
          echo "✓ Found $(basename "$jar_file")"

      - name: Generate cache key
        id: cache-key
        run: echo "key=jar-${{ github.sha }}-${{ github.run_number }}" >> $GITHUB_OUTPUT

      - name: Cache built JAR
        uses: actions/cache/save@v3
        with:
          path: build/libs/*.jar
          key: ${{ steps.cache-key.outputs.key }}
```
