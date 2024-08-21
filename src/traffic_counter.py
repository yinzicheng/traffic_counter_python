import logging
import os
from datetime import datetime
from typing import List, Tuple


class HalfHourlyCar:
    """
    Represents the number of cars for a half-hour interval.

    Attributes:
        timestamp (datetime): The timestamp for the half-hour period.
        cars (int): The number of cars recorded in this period.
    """

    def __init__(self, timestamp: datetime, cars: int):
        self.timestamp = timestamp
        self.cars = cars

    def __str__(self):
        return f"{self.timestamp} {self.cars}"


class DailyCar:
    """
    Represents the number of cars for a full day.

    Attributes:
        date (datetime.date): The date for the day.
        cars (int): The number of cars recorded in this day.
    """

    def __init__(self, date: datetime.date, cars: int):
        self.date = date
        self.cars = cars

    def __str__(self):
        return f"{self.date} {self.cars}"


class TrafficCounter:
    """
    TrafficCounter class is used to count the number of cars that pass a road, based on half-hour intervals.
    It reads data from files in a specified directory.

    Attributes:
        data_dir (str): The directory containing the data files.
        all_half_hourly_cars (List[HalfHourlyCar]): A sorted list of HalfHourlyCar objects based on their timestamps.
    """
    logger = logging.getLogger(__name__)

    def __init__(self, data_dir: str):
        """
        Initializes the TrafficCounter with a specified data directory.

        Args:
            data_dir (str): The directory containing the traffic data files.
        """
        self.data_dir = data_dir
        self.all_half_hourly_cars = sorted(self.get_all_half_hourly_cars(), key=lambda car: car.timestamp)

    @staticmethod
    def line_to_half_hourly_car(line: str, pattern: str = "%Y-%m-%dT%H:%M:%S") -> HalfHourlyCar:
        """
        Converts a line from the input file into a HalfHourlyCar object.

        Args:
            line (str): A line from the input file.
            pattern (str): The datetime pattern to parse the timestamp.

        Returns:
            HalfHourlyCar: An object representing the half-hour interval and car count.
        """
        timestamp_str, cars = line.split()
        timestamp = datetime.strptime(timestamp_str, pattern)
        return HalfHourlyCar(timestamp, int(cars))

    def get_half_hourly_cars_from_file(self, file_path: str) -> List[HalfHourlyCar]:
        """
        Reads a file and converts its content into a list of HalfHourlyCar objects.

        Args:
            file_path (str): The path to the input file.

        Returns:
            List[HalfHourlyCar]: A list of HalfHourlyCar objects parsed from the file.
        """
        try:
            with open(file_path, 'r') as file:
                return [self.line_to_half_hourly_car(line) for line in file if line.strip()]
        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
            return []
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return []

    def get_all_half_hourly_cars(self, file_ext: str = "txt") -> List[HalfHourlyCar]:
        """
        Reads all files in the data directory and aggregates their content into a list of HalfHourlyCar objects.

        Args:
            file_ext (str): The file extension to filter the files (default is "txt").

        Returns:
            List[HalfHourlyCar]: A list of HalfHourlyCar objects from all files.
        """
        cars = []
        if os.path.exists(self.data_dir):
            for file_name in os.listdir(self.data_dir):
                if file_name.endswith(file_ext):
                    file_path = os.path.join(self.data_dir, file_name)
                    cars.extend(self.get_half_hourly_cars_from_file(file_path))
        return cars

    def total_cars(self) -> int:
        """
        Calculates the total number of cars recorded.

        Returns:
            int: The total number of cars.
        """
        return sum(car.cars for car in self.all_half_hourly_cars)

    def daily_cars(self) -> List[DailyCar]:
        """
        Aggregates the car count on a daily basis.

        Returns:
            List[DailyCar]: A list of DailyCar objects, each representing a day's total car count.
        """
        daily_count = {}
        for car in self.all_half_hourly_cars:
            date = car.timestamp.date()
            daily_count[date] = daily_count.get(date, 0) + car.cars
        return [DailyCar(date, count) for date, count in daily_count.items()]

    def get_top_half_hourly_cars(self, top_n: int) -> List[HalfHourlyCar]:
        """
        Retrieves the top N half-hour periods with the highest car counts.

        Args:
            top_n (int): The number of top periods to return.

        Returns:
            List[HalfHourlyCar]: A list of the top N HalfHourlyCar objects.
        """
        return sorted(self.all_half_hourly_cars, key=lambda car: car.cars, reverse=True)[:top_n]

    def get_least_car_of_contiguous_periods(self, period_length: int) -> List[Tuple[int, List[HalfHourlyCar]]]:
        """
        Finds the contiguous periods with the least number of cars.

        Args:
            period_length (int): The length of the contiguous period in terms of half-hour intervals.

        Returns:
            List[Tuple[int, List[HalfHourlyCar]]]: A list of tuples where each tuple contains the total number
                                                   of cars and the corresponding list of HalfHourlyCar objects
                                                   for that period.
        """
        least_cars = []
        for i in range(len(self.all_half_hourly_cars) - period_length + 1):
            period = self.all_half_hourly_cars[i:i + period_length]
            total = sum(car.cars for car in period)
            least_cars.append((total, period))
        return sorted(least_cars, key=lambda x: x[0])
