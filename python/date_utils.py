"""Date and time utilities."""

from datetime import datetime, timedelta
from typing import Optional


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.now().isoformat()


def get_current_date() -> str:
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().strftime('%Y-%m-%d')


def get_current_time() -> str:
    """Get current time in HH:MM:SS format."""
    return datetime.now().strftime('%H:%M:%S')


def format_date(date: datetime, format_str: str = '%Y-%m-%d') -> str:
    """Format datetime object to string."""
    return date.strftime(format_str)


def parse_date(date_str: str, format_str: str = '%Y-%m-%d') -> datetime:
    """Parse string to datetime object."""
    return datetime.strptime(date_str, format_str)


def add_days(date: datetime, days: int) -> datetime:
    """Add days to a date."""
    return date + timedelta(days=days)


def subtract_days(date: datetime, days: int) -> datetime:
    """Subtract days from a date."""
    return date - timedelta(days=days)


def days_between(date1: datetime, date2: datetime) -> int:
    """Calculate days between two dates."""
    return abs((date2 - date1).days)


def is_weekend(date: datetime) -> bool:
    """Check if date is a weekend (Saturday or Sunday)."""
    return date.weekday() in [5, 6]


def get_first_day_of_month(date: Optional[datetime] = None) -> datetime:
    """Get first day of the month."""
    if date is None:
        date = datetime.now()
    return date.replace(day=1)


def get_last_day_of_month(date: Optional[datetime] = None) -> datetime:
    """Get last day of the month."""
    if date is None:
        date = datetime.now()
    next_month = date.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)


def timestamp_to_datetime(timestamp: int) -> datetime:
    """Convert Unix timestamp to datetime object."""
    return datetime.fromtimestamp(timestamp)


def datetime_to_timestamp(date: datetime) -> int:
    """Convert datetime object to Unix timestamp."""
    return int(date.timestamp())


if __name__ == "__main__":
    # Example usage
    print("Date Utilities")
    print(f"Current timestamp: {get_current_timestamp()}")
    print(f"Current date: {get_current_date()}")
    print(f"Current time: {get_current_time()}")
    
    today = datetime.now()
    print(f"Is today weekend? {is_weekend(today)}")
    print(f"First day of month: {get_first_day_of_month()}")
