
# Traffic Counter

## Overview
The Traffic Counter is a Python application designed to analyze traffic data. The application processes data that contains the number of cars passing a certain point on the road during each half-hour interval. It provides useful statistics, such as the total number of cars, daily car counts, and the least number of cars during contiguous periods.

## Features
- **Total Cars**: Calculates the total number of cars recorded.
- **Daily Cars**: Aggregates the car count on a daily basis.
- **Top Hourly Cars**: Retrieves the top N half-hour periods with the highest car counts.
- **Least Car of Contiguous Periods**: Finds the contiguous periods with the least number of cars.

## Directory Structure

```plaintext
traffic_counter/
├── traffic_counter/
│   ├── __init__.py
│   ├── main.py
│   ├── traffic_counter.py
│   ├── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_traffic_counter.py
│   ├── test_utils.py
│   ├── test_main.py
├── README.md
├── setup.py
├── requirements.txt
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd traffic_counter
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Traffic Counter application, you can execute the `main.py` script:

```bash
python -m traffic_counter.main
```

This will output various statistics based on the provided traffic data.

## Running Tests

To run tests, use `pytest`:

```bash
pytest tests/
```

This will execute the test cases and verify that the application behaves as expected.

## License
This project is licensed under the MIT License.
