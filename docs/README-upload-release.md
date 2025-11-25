# 📝 Upload Release Artifact Workflow

## Overview

**Workflow Name:** `Upload Release Artifact`

## Triggers


## Jobs

### `upload`

**Runner:** `ubuntu-latest`

**Steps:**

1. **Download installer artifact**
   - Uses: `actions/download-artifact@v4`
2. **Verify artifact exists**
   - Runs: `echo "=== Files in release-assets ==="...`
3. **Upload to GitHub Release**
   - Uses: `softprops/action-gh-release@v2`

---

*This documentation is auto-generated. Do not edit manually.*
