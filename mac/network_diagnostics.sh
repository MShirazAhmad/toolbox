#!/bin/bash

# Network diagnostics for macOS

echo "=== Network Interfaces ==="
ifconfig | grep -A 2 "^en0\|^en1"
echo ""

echo "=== Active Connections ==="
netstat -an | grep ESTABLISHED | head -10
echo ""

echo "=== DNS Servers ==="
scutil --dns | grep 'nameserver\[[0-9]*\]'
echo ""

echo "=== WiFi Info ==="
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I
echo ""

echo "=== Internet Connectivity Test ==="
ping -c 3 8.8.8.8
