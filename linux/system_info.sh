#!/bin/bash

# Display Linux system information

echo "=== System Information ==="
echo "OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
echo "Kernel: $(uname -r)"
echo "Hostname: $(hostname)"
echo ""

echo "=== CPU Information ==="
lscpu | grep -E "Model name|CPU\(s\)|Thread|Core"
echo ""

echo "=== Memory Information ==="
free -h
echo ""

echo "=== Disk Usage ==="
df -h | grep -E "Filesystem|/dev/"
echo ""

echo "=== Uptime ==="
uptime
echo ""

echo "=== Load Average ==="
cat /proc/loadavg
