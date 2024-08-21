import unittest
import logging
"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

class MyTests(unittest.TestCase):

    def read_log_file(self):
        with open('login_system.log', 'r') as file:
            return file.read()

    def test_log_success(self):
        log_event("user123", "success")
        log_content = self.read_log_file()
        self.assertIn("Login event - Username: user123, Status: success", log_content)

    def test_log_expired(self):
        log_event("user123", "expired")
        log_content = self.read_log_file()
        self.assertIn("Login event - Username: user123, Status: expired", log_content)

    def test_log_failed(self):
        log_event("user123", "failed")
        log_content = self.read_log_file()
        self.assertIn("Login event - Username: user123, Status: failed", log_content)


if __name__ == '__main__':
    unittest.main()
