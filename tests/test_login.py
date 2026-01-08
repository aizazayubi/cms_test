import json
import pytest
from pages.login_page import LoginPage

from utils.helpers import trim_string, generate_long_string

BASE_URL = "http://dev2.sianty.com/login"  # Replace with your login URL

# Load test data
with open("data/credentials.json") as f:
    creds = json.load(f)

# -------- Functional Tests --------
def test_valid_login(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login(creds["valid_user"], creds["valid_pass"])
    assert "/dashboard" in page.url

def test_invalid_password(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login(creds["valid_user"], creds["invalid_pass"])
    assert login.get_error_message().inner_text() == "Invalid username or password"

def test_empty_username(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login("", creds["valid_pass"])
    assert login.get_error_message().inner_text() == "Username is required"

def test_empty_password(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login(creds["valid_user"], "")
    assert login.get_error_message().inner_text() == "Password is required"

# -------- UI Tests --------
def test_login_page_elements_visible(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    assert page.locator(login.username_input).is_visible()
    assert page.locator(login.password_input).is_visible()
    assert page.locator(login.login_button).is_visible()
    assert page.locator(login.forgot_password_link).is_visible()

# -------- Security Tests --------
def test_sql_injection(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login("' OR 1=1--", "' OR 1=1--")
    assert login.get_error_message().inner_text() == "Invalid username or password"

def test_password_masking(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    assert login.is_password_masked()

# -------- Edge Cases --------
def test_leading_trailing_spaces(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login(f"  {creds['valid_user']}  ", creds["valid_pass"])
    assert "/dashboard" in page.url

def test_max_length_fields(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    long_str = generate_long_string(300)
    login.login(long_str, long_str)
    assert login.get_error_message().inner_text() != ""  # Should show error

def test_empty_credentials(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login("", "")
    assert login.get_error_message().inner_text() == "Username and Password are required"

# -------- Performance Test --------
def test_login_performance(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    with page.expect_navigation(timeout=5000):
        login.login(creds["valid_user"], creds["valid_pass"])
    assert "/dashboard" in page.url
