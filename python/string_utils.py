"""String manipulation utilities."""

import re
from typing import List


def camel_to_snake(text: str) -> str:
    """Convert camelCase to snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


def snake_to_camel(text: str) -> str:
    """Convert snake_case to camelCase."""
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def title_case(text: str) -> str:
    """Convert string to Title Case."""
    return text.title()


def remove_whitespace(text: str) -> str:
    """Remove all whitespace from string."""
    return ''.join(text.split())


def truncate(text: str, length: int, suffix: str = '...') -> str:
    """Truncate string to specified length with suffix."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def count_words(text: str) -> int:
    """Count words in a string."""
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Check if string is a palindrome (ignoring case and spaces)."""
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]


def split_by_delimiter(text: str, delimiter: str = ',') -> List[str]:
    """Split string by delimiter and strip whitespace."""
    return [item.strip() for item in text.split(delimiter)]


def join_with_delimiter(items: List[str], delimiter: str = ', ') -> str:
    """Join list of strings with delimiter."""
    return delimiter.join(items)


def extract_numbers(text: str) -> List[int]:
    """Extract all numbers from a string."""
    return [int(num) for num in re.findall(r'\d+', text)]


if __name__ == "__main__":
    # Example usage
    print("String Utilities")
    print(f"camel_to_snake('camelCase'): {camel_to_snake('camelCase')}")
    print(f"snake_to_camel('snake_case'): {snake_to_camel('snake_case')}")
    print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
