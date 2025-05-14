#!/bin/bash

# Get current date and time for the commit message
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Add all changes
git add .

# Commit with timestamp
git commit -m "Auto-commit: $TIMESTAMP"

# Push to the current branch
git push

echo "Changes committed and pushed with timestamp: $TIMESTAMP"
