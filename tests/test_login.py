def test_login(login_page, dashboard_page, credentials):
    login_page.open(credentials["baseUrl"])
    login_page.login(credentials["username"], credentials["password"])
    dashboard_page.wait_loaded()
def test_login(login_page, dashboard_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login(credentials["username"], credentials["password"])
    dashboard_page.wait_loaded()
def test_invalid_login(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login("invalid_user", "wrong_password")
    error_message = login_page.get_error_message()
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Invalid username or password.")
def test_invalid_login(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login("invalid_user", "wrong_password")
    error_message = login_page.get_error_message()
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Invalid username or password.")
def test_password_masking(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    is_masked = login_page.is_password_masked()
    assert is_masked, "Password input field is not masked"
def test_password_masking(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    is_masked = login_page.is_password_masked()
    assert is_masked, "Password input field is not masked"
def test_login(login_page, dashboard_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login(credentials["username"], credentials["password"])
    dashboard_page.wait_loaded()
    



def test_invalid_login(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login("invalid_user", "wrong_password")
    error_message = login_page.get_error_message()
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Invalid username or password.")
def test_password_masking(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    is_masked = login_page.is_password_masked()
    assert is_masked, "Password input field is not masked"
def test_login(login_page, dashboard_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login(credentials["username"], credentials["password"])
    dashboard_page.wait_loaded()
def test_invalid_login(login_page, credentials):
    login_page.goto(credentials["baseUrl"])
    login_page.login("invalid_user", "wrong_password")
    error_message = login_page.get_error_message()
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Invalid username or password.")