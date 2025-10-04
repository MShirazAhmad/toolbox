#!/bin/bash

# Clean up macOS system caches and temporary files

echo "Starting macOS cleanup..."

# Clear user cache
echo "Clearing user cache..."
rm -rf ~/Library/Caches/*

# Clear system logs (older than 7 days)
echo "Clearing old system logs..."
sudo rm -rf /private/var/log/*.log.*.gz
sudo rm -rf /Library/Logs/*.log.*.gz

# Empty trash
echo "Emptying trash..."
rm -rf ~/.Trash/*

# Clear DNS cache
echo "Flushing DNS cache..."
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Clear download history
echo "Clearing download history..."
rm -f ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2

echo "Cleanup complete!"
echo "You may need to restart your Mac for all changes to take effect."
