"""Common file operations utilities."""

import os
import shutil
from pathlib import Path
from typing import List


def read_file(filepath: str) -> str:
    """Read entire file content as string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath: str, content: str) -> None:
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def read_lines(filepath: str) -> List[str]:
    """Read file content as list of lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()


def append_to_file(filepath: str, content: str) -> None:
    """Append content to file."""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)


def copy_file(src: str, dst: str) -> None:
    """Copy file from source to destination."""
    shutil.copy2(src, dst)


def move_file(src: str, dst: str) -> None:
    """Move file from source to destination."""
    shutil.move(src, dst)


def delete_file(filepath: str) -> None:
    """Delete a file."""
    os.remove(filepath)


def file_exists(filepath: str) -> bool:
    """Check if file exists."""
    return os.path.isfile(filepath)


def get_file_size(filepath: str) -> int:
    """Get file size in bytes."""
    return os.path.getsize(filepath)


def list_files(directory: str, extension: str = None) -> List[str]:
    """List all files in directory, optionally filtered by extension."""
    path = Path(directory)
    if extension:
        return [str(f) for f in path.glob(f'*.{extension}')]
    return [str(f) for f in path.glob('*') if f.is_file()]


def create_directory(directory: str) -> None:
    """Create directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)


if __name__ == "__main__":
    # Example usage
    print("File Operations Utilities")
    print("Import these functions in your Python scripts")
