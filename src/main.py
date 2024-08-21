import logging

from traffic_counter import TrafficCounter


def main(args=None):
    """
    Entry point for the Traffic Counter application.

    Args:
        args (list): Command-line arguments. The first argument should be the data directory.
                     If no arguments are provided, it defaults to "src/main/resources/data/".
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set default data directory if no arguments are provided
    if args is None:
        args = ["src/main/resources/data/"]

    # Log the received parameters
    logger.info(f"Main Parameters: {' '.join(args)}")

    # Determine the data directory from the arguments
    data_dir = args[0] if len(args) > 0 else "src/main/resources/data/"

    # Initialize TrafficCounter with the specified data directory
    counter = TrafficCounter(data_dir)

    # Log the results of various analyses
    logger.info(f"\n1. Total cars:\n{counter.total_cars()}")
    logger.info(f"\n2. Daily cars:\n{counter.daily_cars()}")
    logger.info(f"\n3. Top 3 hourly cars:\n{counter.get_top_half_hourly_cars(3)}")
    logger.info(f"\n4. Least Car of Contiguous Periods:\n{counter.get_least_car_of_contiguous_periods(3)}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
