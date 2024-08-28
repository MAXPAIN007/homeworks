import pytest
from lesson10.homework_10 import log_event
from assertpy import assert_that

class TestsLogger:

    def read_log_file(self):
        with open('login_system.log', 'r') as file:
            return file.read()

    def test_log_success(self):
        log_event("user123", "success")
        log_content = self.read_log_file()
        # assert "Login event - Username: user123, Status: success" in log_content
        assert_that(log_content).contains("Login event - Username: user123, Status: success")

    def test_log_expired(self):
        log_event("user123", "expired")
        log_content = self.read_log_file()
        assert_that(log_content).contains("Login event - Username: user123, Status: expired")

    def test_log_failed(self):
        log_event("user123", "failed")
        log_content = self.read_log_file()
        assert_that(log_content).contains("Login event - Username: user123, Status: failed")

