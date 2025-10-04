#!/bin/bash

# Display macOS system information

echo "=== System Information ==="
echo "macOS Version: $(sw_vers -productVersion)"
echo "Build: $(sw_vers -buildVersion)"
echo "Hostname: $(hostname)"
echo ""

echo "=== Hardware ==="
system_profiler SPHardwareDataType | grep -E "Model Name|Model Identifier|Processor|Memory|Serial"
echo ""

echo "=== Disk Usage ==="
df -h / | awk 'NR==1 || /\/$/'
echo ""

echo "=== Uptime ==="
uptime
