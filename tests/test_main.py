from pathlib import Path

import pytest

from main import main


@pytest.fixture
def mock_traffic_counter(mocker):
    """
    Fixture to mock the TrafficCounter class and its methods.
    """
    mock_traffic_counter = mocker.patch('main.TrafficCounter')
    instance = mock_traffic_counter.return_value
    instance.total_cars.return_value = 100
    instance.daily_cars.return_value = []
    instance.get_top_half_hourly_cars.return_value = []
    instance.get_least_car_of_contiguous_periods.return_value = []
    return mock_traffic_counter


def test_main(mock_traffic_counter):
    """
    Test for the main function.
    """
    main()

    root_path = Path(__file__).parent.parent
    data_dir = str(Path(root_path, 'src', 'resources', 'data'))

    mock_traffic_counter.assert_called_once_with(data_dir)
    mock_traffic_counter.return_value.total_cars.assert_called_once()
    mock_traffic_counter.return_value.daily_cars.assert_called_once()
    mock_traffic_counter.return_value.get_top_half_hourly_cars.assert_called_once_with(3)
    mock_traffic_counter.return_value.get_least_car_of_contiguous_periods.assert_called_once_with(3)
