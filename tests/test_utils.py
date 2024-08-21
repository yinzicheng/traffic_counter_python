from datetime import datetime

from utils import timestamp_to_date


def test_timestamp_to_date():
    """
    Test for the timestamp_to_date function.
    """
    timestamp = datetime(2023, 8, 20, 8, 0)
    date = timestamp_to_date(timestamp)
    assert date == timestamp.date()
    assert str(date) == "2023-08-20"
