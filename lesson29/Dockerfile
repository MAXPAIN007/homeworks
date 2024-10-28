#FROM python:3.9
#
#WORKDIR /app
#
## Копіюємо всі файли
#COPY requirements.txt /app/requirements.txt
#COPY test_db.py /app/test_db.py
#COPY db_config.py /app/db_config.py
#
## Встановлюємо залежності
#RUN pip install -r requirements.txt
#
## Запускаємо тест
#CMD ["pytest", "/app/test_db.py"]

FROM python:3.9

WORKDIR /app

# Скопировать wait-for-it.sh в образ
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Копируем необходимые файлы
COPY requirements.txt /app/requirements.txt
COPY test_db.py /app/test_db.py
COPY db_config.py /app/db_config.py
COPY wait-for-it.sh /app/wait-for-it.sh

# Устанавливаем зависимости
RUN pip install -r requirements.txt
RUN chmod +x /app/wait-for-it.sh

# Используем wait-for-it.sh для ожидания базы данных перед запуском тестов
CMD ["/app/wait-for-it.sh", "db:5432", "--", "pytest", "test_db.py"]

