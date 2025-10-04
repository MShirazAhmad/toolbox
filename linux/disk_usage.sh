#!/bin/bash

# Analyze disk usage by directory

echo "=== Top 10 Largest Directories ==="
du -h --max-depth=1 / 2>/dev/null | sort -hr | head -10
echo ""

echo "=== Current Directory Usage ==="
du -h --max-depth=1 . | sort -hr
echo ""

echo "=== Find Large Files (>100MB) ==="
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | head -10
