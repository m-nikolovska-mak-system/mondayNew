import os
from datetime import datetime

README_PATH = "README.md"
marker = "<!-- AUTO-GENERATED-SECTION -->"

new_section = f"""
{marker}
_Last updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}_
"""

if os.path.exists(README_PATH):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
else:
    content = "# 🧾 Project Overview\n"

if marker in content:
    # Replace the old section with the new one
    start = content.index(marker)
    content = content[:start] + new_section
else:
    # Append new section
    content += "\n" + new_section

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ README updated with timestamp in {README_PATH}")
