from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = 'input[name="email"]'     # updated
        self.password_input = 'input[name="password"]'  # updated
        self.login_button = '//*[@id="form"]/div[5]/button'  # xpath
        self.error_msg = ".error"  # Adjust if your app shows errors differently

    def goto(self, url: str):
        self.page.goto(url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.locator(self.error_msg)

    def is_password_masked(self):
        return self.page.get_attribute(self.password_input, "type") == "password"
