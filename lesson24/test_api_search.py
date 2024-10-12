import pytest
import logging
from assertpy import assert_that
from requests import Session


log_file_path = r"C:\Users\007\PycharmProjects\homeworks\lesson24\test_search.log"

logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

file_handler = logging.FileHandler(log_file_path, mode='a')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("Logging initiated.")



BASE_URL = "http://127.0.0.1:8080"

# Параметризация: 5-7 наборов данных с разными параметрами для GET
@pytest.mark.parametrize(
    "sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        (None, None),
        ("brand", 10),
        ("price", None),
        ("year", 20)
    ]
)
class TestCarAPISearch:

    def test_get_desired_car(self, authorization: Session, sort_by, limit):
        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if limit:
            params['limit'] = limit

        response = authorization.get(f"{BASE_URL}/cars", params=params)

        logger.info(f"GET /cars with params sort_by={sort_by}, limit={limit}")
        assert_that(response.status_code).is_equal_to(200)

        cars = response.json()
        assert_that(cars).is_not_empty()

        logger.info("Response data: %s", cars)

        print(f"\nTest: Sort by '{sort_by}' with limit {limit}")
        print(f"Received {len(cars)} cars")
        print(f"List of cars: {[car['brand'] for car in cars]}")
