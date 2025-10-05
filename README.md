# toolbox

Nanoindentation Colab Link: https://colab.research.google.com/github/MShirazAhmad/toolbox/blob/main/python/nanoindentation/Nanoindentation.ipynb

Personal collection of reusable code snippets for Mac, Linux, and Python.

## 📁 Repository Structure

```
toolbox/
├── mac/           # macOS-specific scripts and utilities
├── linux/         # Linux-specific scripts and utilities
└── python/        # Python utilities and helper functions
```

## 🍎 Mac Snippets

Collection of macOS-specific commands and shell scripts.

**Contents:**
- `system_info.sh` - Display comprehensive system information
- `cleanup.sh` - Clean up system caches and temporary files
- `network_diagnostics.sh` - Network diagnostics and troubleshooting tools

[View Mac snippets →](mac/)

## 🐧 Linux Snippets

Collection of Linux commands, scripts, and utilities.

**Contents:**
- `system_info.sh` - Display system information and hardware details
- `disk_usage.sh` - Analyze disk usage by directory and find large files
- `process_monitor.sh` - Monitor CPU and memory consuming processes
- `backup.sh` - Simple backup script for directories

[View Linux snippets →](linux/)

## 🐍 Python Snippets

Reusable Python utilities and helper functions for common tasks.

**Contents:**
- `file_operations.py` - File I/O operations and directory management
- `string_utils.py` - String manipulation and transformation utilities
- `date_utils.py` - Date and time handling utilities
- `http_client.py` - Simple HTTP client examples
- `json_utils.py` - JSON parsing, validation, and manipulation

[View Python snippets →](python/)

## 🚀 Usage

### Shell Scripts (Mac/Linux)

1. Make the script executable:
   ```bash
   chmod +x script_name.sh
   ```

2. Run the script:
   ```bash
   ./script_name.sh
   ```

### Python Utilities

Import utilities directly in your Python code:

```python
from python.file_operations import read_file, write_file
from python.string_utils import camel_to_snake
from python.date_utils import get_current_timestamp

# Use the functions
content = read_file('example.txt')
snake_case = camel_to_snake('camelCaseString')
timestamp = get_current_timestamp()
```

Or run scripts directly:
```bash
python python/script_name.py
```

## 📝 Contributing

This is a personal toolbox, but feel free to:
- Fork this repository for your own use
- Suggest improvements via issues
- Use these snippets in your own projects

## 📄 License

MIT License - feel free to use these snippets in your projects!
