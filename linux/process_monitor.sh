#!/bin/bash

# Monitor top processes

echo "=== Top 10 CPU Consuming Processes ==="
ps aux --sort=-%cpu | head -11
echo ""

echo "=== Top 10 Memory Consuming Processes ==="
ps aux --sort=-%mem | head -11
echo ""

echo "=== Process Count by User ==="
ps aux | awk '{print $1}' | sort | uniq -c | sort -rn
echo ""

echo "=== System Resource Summary ==="
echo "Total Processes: $(ps aux | wc -l)"
echo "Running Processes: $(ps aux | grep -c " R ")"
echo "Sleeping Processes: $(ps aux | grep -c " S ")"
