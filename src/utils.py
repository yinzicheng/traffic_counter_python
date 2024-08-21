from datetime import datetime


def timestamp_to_date(timestamp: datetime, pattern: str = "%Y-%m-%d") -> datetime.date:
    """
    Converts a timestamp to a date using the specified pattern.

    Args:
        timestamp (datetime): The timestamp to convert.
        pattern (str): The pattern to use for conversion (default is "%Y-%m-%d").

    Returns:
        datetime.date: The corresponding date object.
    """
    return datetime.strptime(timestamp.strftime(pattern), pattern).date()
