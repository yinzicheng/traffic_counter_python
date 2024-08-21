import pytest
from main import main


@pytest.fixture
def mock_traffic_counter(mocker):
    """
    Fixture to mock the TrafficCounter class and its methods.
    """
    MockTrafficCounter = mocker.patch('main.TrafficCounter')
    instance = MockTrafficCounter.return_value
    instance.total_cars.return_value = 100
    instance.daily_cars.return_value = []
    instance.get_top_half_hourly_cars.return_value = []
    instance.get_least_car_of_contiguous_periods.return_value = []
    return MockTrafficCounter


def test_main(mock_traffic_counter):
    """
    Test for the main function.
    """
    main()

    mock_traffic_counter.assert_called_once_with("src/main/resources/data/")
    mock_traffic_counter.return_value.total_cars.assert_called_once()
    mock_traffic_counter.return_value.daily_cars.assert_called_once()
    mock_traffic_counter.return_value.get_top_half_hourly_cars.assert_called_once_with(3)
    mock_traffic_counter.return_value.get_least_car_of_contiguous_periods.assert_called_once_with(3)
