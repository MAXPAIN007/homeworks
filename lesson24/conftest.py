import pytest
import requests
import os
from assertpy import assert_that
from dotenv import load_dotenv
from requests import Response, Session
from requests.auth import HTTPBasicAuth


load_dotenv("user_data.env")
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

BASE_URL:str ="http://127.0.0.1:8080"

@pytest.fixture(scope="session", autouse=True)
def authorization() -> None:

    auth = HTTPBasicAuth(db_user, db_password)

    response: Response = requests.post(f"{BASE_URL}/auth", auth=auth, verify=False)

    assert_that(response.status_code).is_equal_to(200)
    access_token: str = response.json().get("access_token")
    current_session = Session()
    current_session.headers.update({'Authorization': 'Bearer ' + access_token})

    yield current_session