#!/bin/bash

# Simple backup script
# Usage: ./backup.sh <source_directory> <backup_directory>

if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <backup_directory>"
    exit 1
fi

SOURCE_DIR="$1"
BACKUP_DIR="$2"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_${DATE}.tar.gz"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist: $SOURCE_DIR"
    exit 1
fi

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "Starting backup..."
echo "Source: $SOURCE_DIR"
echo "Destination: $BACKUP_DIR/$BACKUP_NAME"

# Create compressed backup
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup file: $BACKUP_DIR/$BACKUP_NAME"
    echo "Size: $(du -h "$BACKUP_DIR/$BACKUP_NAME" | cut -f1)"
else
    echo "Backup failed!"
    exit 1
fi
