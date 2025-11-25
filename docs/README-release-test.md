# 📝 Test Release Workflow Workflow

## Overview

**Workflow Name:** `Test Release Workflow`

## Triggers


## Jobs

### `print-release-info`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Show release info**
   - Runs: `echo "Release tag: ${{ github.event.release.tag_name }}"...`

---

*This documentation is auto-generated. Do not edit manually.*
