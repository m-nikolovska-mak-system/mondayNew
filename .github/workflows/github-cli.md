## 🚀 Creating and Managing GitHub Releases with `gh` CLI

The GitHub CLI lets you perform almost anything you can do on the GitHub website, but directly from your terminal or inside a workflow. 

We use the **GitHub CLI (`gh`)** to automate release creation and version tagging.  
This ensures that our tags and release notes stay consistent across environments.

### 🧩 1. What tags and releases mean

- **Tag** → a Git reference pointing to a specific commit (e.g. `v1.3.0`)
- **Release** → a GitHub record built on top of a tag, including notes, assets, or changelogs

A release *must* be linked to an existing tag — GitHub won’t allow duplicates.

---

### ⚙️ 2. Creating a new tag locally

```bash
# Create a new version tag
git tag -a v1.3.1 -m "Release v1.3.1"

# Push the tag to GitHub
git push origin v1.3.1


# To verify
git tag -n5    # lists recent tags with notes


```


### 🪄 3. Creating a GitHub release from the tag


```bash
gh release create v1.3.1 --title "v1.3.1" --notes "Release test for v1.3.1"
```
✅ This command automatically links the tag to a new GitHub release and publishes it with the specified notes.



### ⚠️ 4. Handling common errors

If you see:

```bash
HTTP 422: Validation Failed
Release.tag_name already exists
```


It means a release for that tag already exists.
You can either:

##### Edit existing release:

```bash
gh release edit v1.3.1 --notes "Updated release notes"
```

##### Delete and recreate it:
```bash
gh release delete v1.3.1
gh release create v1.3.1 --title "v1.3.1" --notes "Recreated release"
```


##### Or create a new tag and release:

```bash
git tag -a v1.3.2 -m "Release v1.3.2"
git push origin v1.3.2
gh release create v1.3.2 --title "v1.3.2" --notes "Next version release"
```

#### 📋 5. Checking existing releases and tags


```bash
# List all releases
gh release list

# List all local tags
git tag -n
```