"""
File reading utilities for common file operations.
"""

def read_file_lines(filepath, strip=True):
    """
    Read a file and return its lines as a list.
    
    Args:
        filepath (str): Path to the file to read
        strip (bool): Whether to strip whitespace from each line
        
    Returns:
        list: List of lines from the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if strip:
            lines = [line.strip() for line in lines]
        return lines


def read_file_content(filepath):
    """
    Read entire file content as a single string.
    
    Args:
        filepath (str): Path to the file to read
        
    Returns:
        str: File content
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


# Usage examples:
if __name__ == "__main__":
    # Example 1: Read lines
    # lines = read_file_lines('example.txt')
    # for line in lines:
    #     print(line)
    
    # Example 2: Read full content
    # content = read_file_content('example.txt')
    # print(content)
    pass
