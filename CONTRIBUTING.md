# Contributing to Toolbox

Thank you for your interest in contributing to this code snippet repository!

## 📋 Guidelines for Adding Snippets

### File Organization

1. **Choose the right directory**: Place your snippet in the most appropriate category
2. **Create subdirectories**: If needed, create logical subdirectories within categories
3. **Naming conventions**: Use descriptive, lowercase names with hyphens (e.g., `binary-search.py`, `array-helpers.js`)

### Code Quality Standards

#### Documentation
- Add clear comments explaining what the code does
- Include docstrings/JSDoc for functions and classes
- Document parameters, return values, and exceptions

#### Examples
```python
# Python example
def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr (list): Sorted array to search
        target: Element to find
        
    Returns:
        int: Index of target if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Implementation here
    pass

# Usage example:
# result = binary_search([1, 2, 3, 4, 5], 3)
# print(result)  # Output: 2
```

### Required Information

Each snippet should include:

1. **Purpose**: What problem does it solve?
2. **Usage example**: How to use the code
3. **Dependencies**: Required libraries or packages
4. **Complexity analysis** (for algorithms): Time and space complexity
5. **Edge cases**: Any limitations or special cases

### Language-Specific Guidelines

#### Python
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for all functions and classes

#### JavaScript/TypeScript
- Use ES6+ syntax
- Include JSDoc/TSDoc comments
- TypeScript snippets must include type annotations

#### Shell/Bash
- Include shebang line (#!/bin/bash or #!/bin/sh)
- Add usage instructions in comments
- Handle errors appropriately

## 📁 Directory Structure

When adding new snippets:
- Update the relevant directory's README.md
- Create subdirectories for related snippets
- Maintain consistent structure within categories

## ✅ Checklist Before Adding

- [ ] Code is well-documented
- [ ] Usage example is included
- [ ] Dependencies are listed
- [ ] Code follows language conventions
- [ ] Snippet is placed in the correct directory
- [ ] README updated if needed

## 🔍 Testing

While not strictly required for all snippets:
- Test your code before adding it
- Include test cases for complex algorithms
- Verify edge cases are handled

## 🚀 Workflow

1. Create a new branch for your snippet
2. Add your code to the appropriate directory
3. Update relevant README files
4. Test your code
5. Commit with a clear message
6. Submit a pull request (if applicable)

## 💬 Questions?

If you're unsure about where to place a snippet or have questions about the guidelines, feel free to open an issue for discussion.

## 📝 Commit Message Format

Use clear, descriptive commit messages:
```
Add binary search algorithm in Python
Update database connection utility
Fix bug in array rotation function
```

## 🎯 Goal

The goal is to maintain a clean, organized, and useful collection of code snippets that can be easily found and reused across projects.

Thank you for contributing! 🙏
