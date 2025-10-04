"""Simple HTTP client examples using requests library."""

import json
from typing import Dict, Any, Optional

try:
    import requests
except ImportError:
    print("requests library not installed. Install with: pip install requests")
    requests = None


def get_request(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Perform GET request."""
    if requests is None:
        return {"error": "requests library not installed"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def post_request(url: str, data: Dict[str, Any], 
                 headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Perform POST request."""
    if requests is None:
        return {"error": "requests library not installed"}
    
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()


def put_request(url: str, data: Dict[str, Any],
                headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Perform PUT request."""
    if requests is None:
        return {"error": "requests library not installed"}
    
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    
    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()


def delete_request(url: str, headers: Optional[Dict[str, str]] = None) -> bool:
    """Perform DELETE request."""
    if requests is None:
        return False
    
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code in [200, 204]


def download_file(url: str, filepath: str) -> bool:
    """Download file from URL."""
    if requests is None:
        return False
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    return True


if __name__ == "__main__":
    print("HTTP Client Utilities")
    print("Import these functions to make HTTP requests in your Python scripts")
    print("Note: Requires 'requests' library (pip install requests)")
