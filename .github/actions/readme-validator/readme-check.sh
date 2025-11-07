#!/bin/bash
# README validation script

# Add your validation logic here
# This is just a placeholder that the linter found

set -e  # Exit on any error

find . -name "*.sh" -type f -exec chmod +x {} \;


echo "Running README checks..."

if [ ! -f "README.md" ]; then
    echo "❌ Error: README.md not found!"
    exit 1
fi

echo "✅ README.md exists"