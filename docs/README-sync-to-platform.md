# Sync to Platform Repo

> **Type:** Automated  
> **Source:** `sync-to-platform.yml`

## 📋 Overview

This document provides comprehensive documentation for the `Sync to Platform Repo` workflow.

---

## 🎯 Triggers

- **`release`**
  - Types: `published`

---

## 📥 Inputs

_This workflow does not accept any inputs._

---

## 📤 Outputs

_This workflow does not expose any outputs._

---

## 🔐 Secrets

_This workflow does not require any secrets._

---

## 💼 Jobs

### 🔧 `sync-to-platform`

_No steps defined._


---

## 📄 Full Workflow YAML

<details>
<summary>Click to expand full YAML definition</summary>

```yaml
# ========================================
# CALLER WORKFLOW - Product Team A
# ========================================
# 
# This workflow syncs ONLY configuration files and documentation
# to the platform repository when a release is published.
#
# Files synced:
# - All YAML config files
# - README and documentation
# - Build scripts
# ========================================

name: Sync to Platform Repo

# Trigger: Run whenever a GitHub release is published
on:
  release:
    types: [published]

jobs:
  sync-to-platform:
    name: Sync Files to Platform
    
    # Call the reusable workflow
    uses: m-nikolovska-mak-system/reusable-actions-library/.github/workflows/sync-to-platform-reusable.yml@main
    
    with:
      # ────────────────────────────────────
      # WHAT TO SYNC
      # ────────────────────────────────────
      # Only sync specific file patterns (one per line)
      # CUSTOMIZE THIS: Add your actual files here
      source_files: |
        oneProjectWed/src/java/com/miha/app/App.java
        README.md
      
      
      # Sync only files that changed since last release
      sync_mode: 'changed'
      
      # ────────────────────────────────────
      # WHERE TO SYNC
      # ────────────────────────────────────
      # Destination repository (CHANGE THIS to your platform repo)
      destination_repo: 'm-nikolovska-mak-system/platform-repo'
      
      # Files will be copied to: platform-repo/products/my-java-app/
      destination_path: 'products/mondayNew'
      
      # Keep the same folder structure (config/app.yml stays as config/app.yml)
      preserve_structure: true
      
      # ────────────────────────────────────
      # TAGGING & COMMIT OPTIONS
      # ────────────────────────────────────
      # Create a matching tag in the platform repo
      create_tag: true
      
      # Add prefix to distinguish from other products
      # v1.2.3 becomes → my-java-app-v1.2.3
      tag_prefix: 'my-java-app-'
      
      # Commit message
      commit_message_template: '🔄 Sync from {repo} release {tag} ({files} files)'
    
    secrets:
      # PAT token for writing to destination repo
      # Setup: Repository Settings → Secrets → Actions → New secret
      # Name: PLATFORM_PAT
      # Value: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
      destination_token: ${{ secrets.PLATFORM_PAT }}
```

</details>

---

**Generated on:** 2025-12-16 09:48:44 UTC
