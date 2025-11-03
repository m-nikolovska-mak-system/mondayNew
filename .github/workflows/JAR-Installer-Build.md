# 🔄 Automated Build & Release Workflows (Java JAR + Windows Installer)

This repository includes **two GitHub Actions workflows** that automate:

✅ Building a Java JAR file using Gradle  
✅ Creating a Windows installer (`.exe`) using Inno Setup  
✅ Uploading the installer to a GitHub Release  

---

## 📂 Workflow Files

### 1. **Main Build and Release**  
File: `.github/workflows/main-build.yml`  
**Purpose:**  
- Triggered when a **GitHub Release** is created or manually via **Actions → Run workflow**.
- Builds the JAR file.
- Caches the JAR for reuse.
- Calls the reusable installer workflow.
- Uploads the final `.exe` installer to the Release page.

---

### 2. **Build Installer (Reusable)**  
File: `.github/workflows/build-installer.yml`  
**Purpose:**  
- Builds the Windows installer using **Inno Setup**.
- Designed as a **reusable workflow** that can be called from other workflows.
- Uploads the installer as an artifact for the calling workflow.

---

## ✅ How It Works (Step-by-Step)

1. **Developer creates a GitHub Release** (or triggers manually).
2. `main-build.yml`:
   - Checks out the code.
   - Builds the JAR with Gradle.
   - Saves the JAR in a cache.
   - Calls `build-installer.yml` and passes the cache key.
3. `build-installer.yml`:
   - Restores the cached JAR.
   - Renames it to `App.jar`.
   - Installs Inno Setup via Chocolatey.
   - Compiles the installer using `setup-script.iss`.
   - Uploads the installer as an artifact.
4. Back in `main-build.yml`:
   - Downloads the installer artifact.
   - Uploads it to the GitHub Release.

---

## 🔧 How to Reuse for Your Project
### **1. Copy the workflows**
- Place both files in `.github/workflows/` in your repo.

### **2. Update Inno Setup script**
- Edit `setup-script.iss` in your repo:
  - Change `OutputBaseFilename` to your desired installer name:
    ```iss
    OutputBaseFilename=MyAppInstaller
    ```
- Ensure the script points to `App.jar` (since the workflow renames the JAR).

### **3. Update workflow paths and names**
- In both workflows, update:
  - `files: output/MyAppInstaller.exe` (in `upload-to-release` step).
  - Artifact name if needed (`setup-installer`).

### **4. Test manually**
- Go to **Actions → Main Build and Release → Run workflow**.
- Check:
  - JAR built successfully.
  - Installer artifact uploaded.
  - Installer attached to the Release.

---

## ✅ Best Practices

- **Keep `build-installer.yml` generic**:
  - It should only depend on the JAR and the `.iss` script.
  - This makes it reusable across multiple projects.

- **Use cache for JAR**:
  - Speeds up builds and avoids re-uploading large files.

- **Secrets**:
  - `GITHUB_TOKEN` is provided by GitHub automatically.
  - No extra secrets needed unless you add custom steps.

---

## 📌 Example Trigger

- Create a new release:
  - Tag: `v1.0.0`
  - Title: `First Release`
- Workflow runs automatically and uploads `MyAppInstaller.exe` to the release.

---
