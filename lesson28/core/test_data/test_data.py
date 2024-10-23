import os
from dotenv import load_dotenv

load_dotenv("C:\\Users\\007\\PycharmProjects\\homeworks\\lesson28\\core\\test_data\\user_data.env")

class TestData:

    login = os.getenv("INCOMING_LOGIN")
    password = os.getenv("INCOMING_PASS")

    BASE_URL:str = f"https://{login}:{password}@qauto2.forstudy.space"

print(TestData.BASE_URL)