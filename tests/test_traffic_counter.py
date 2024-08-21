from datetime import datetime

import pytest
from traffic_counter import TrafficCounter, HalfHourlyCar


@pytest.fixture
def mock_data():
    """
    Fixture to provide mock data for testing.
    """
    return [
        HalfHourlyCar(datetime(2023, 8, 20, 8, 0), 10),
        HalfHourlyCar(datetime(2023, 8, 20, 8, 30), 20),
        HalfHourlyCar(datetime(2023, 8, 20, 9, 0), 5)
    ]


@pytest.fixture
def traffic_counter(tmpdir, mock_data):
    """
    Fixture to provide a TrafficCounter instance for testing.
    """
    data_dir = tmpdir.mkdir("data")
    file = data_dir.join("traffic.txt")
    file.write("\n".join([f"{car.timestamp.strftime('%Y-%m-%dT%H:%M:%S')} {car.cars}" for car in mock_data]))

    return TrafficCounter(str(data_dir))


def test_total_cars(mock_data, traffic_counter):
    """
    Test for the total_cars function.
    """
    assert traffic_counter.total_cars() == sum(car.cars for car in mock_data)


def test_daily_cars(mock_data, traffic_counter):
    """
    Test for the daily_cars function.
    """
    daily_cars = traffic_counter.daily_cars()
    assert len(daily_cars) == 1
    assert daily_cars[0].cars == sum(car.cars for car in mock_data)
    assert daily_cars[0].date == mock_data[0].timestamp.date()


def test_get_top_half_hourly_cars(mock_data, traffic_counter):
    """
    Test for the get_top_half_hourly_cars function.
    """
    top_cars = traffic_counter.get_top_half_hourly_cars(1)
    assert len(top_cars) == 1
    assert top_cars[0].cars == max(car.cars for car in mock_data)


def test_get_least_car_of_contiguous_periods(mock_data, traffic_counter):
    """
    Test for the get_least_car_of_contiguous_periods function.
    """
    least_cars = traffic_counter.get_least_car_of_contiguous_periods(2)
    assert len(least_cars) == 2
    assert least_cars[0][0] == mock_data[1].cars + mock_data[2].cars


def test_line_to_half_hourly_car(mock_data):
    """
    Test for the line_to_half_hourly_car static method.
    """
    line = "2023-08-20T08:00:00 10"
    half_hourly_car = TrafficCounter._line_to_half_hourly_car(line)
    assert half_hourly_car.timestamp == datetime(2023, 8, 20, 8, 0)
    assert half_hourly_car.cars == 10


def test_get_half_hourly_cars_from_file(traffic_counter):
    """
    Test for the get_half_hourly_cars_from_file method.
    """
    half_hourly_cars = traffic_counter._get_half_hourly_cars_from_file(traffic_counter.data_dir + "/traffic.txt")
    assert len(half_hourly_cars) == 3
