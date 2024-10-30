import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",  # db - контейнер PostgreSQL у Docker
        port="5432"
    )