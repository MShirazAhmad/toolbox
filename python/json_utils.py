"""JSON handling utilities."""

import json
from typing import Any, Dict


def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load JSON from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json_file(filepath: str, data: Dict[str, Any], indent: int = 2) -> None:
    """Save data to JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def json_to_string(data: Dict[str, Any], indent: int = 2) -> str:
    """Convert Python object to JSON string."""
    return json.dumps(data, indent=indent, ensure_ascii=False)


def string_to_json(json_str: str) -> Dict[str, Any]:
    """Parse JSON string to Python object."""
    return json.loads(json_str)


def pretty_print_json(data: Dict[str, Any]) -> None:
    """Pretty print JSON data."""
    print(json.dumps(data, indent=2, ensure_ascii=False))


def merge_json(json1: Dict[str, Any], json2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two JSON objects (json2 overwrites json1)."""
    merged = json1.copy()
    merged.update(json2)
    return merged


def flatten_json(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten nested JSON structure."""
    items = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def validate_json(json_str: str) -> bool:
    """Validate if string is valid JSON."""
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False


if __name__ == "__main__":
    # Example usage
    print("JSON Utilities")
    
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    }
    
    print("\nOriginal JSON:")
    pretty_print_json(sample_data)
    
    print("\nFlattened JSON:")
    pretty_print_json(flatten_json(sample_data))
