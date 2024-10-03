from playwright.sync_api import Page

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page : Page) -> None:
        self.page = page
        self.user_name = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def load(self) -> None:
            self.page.goto(self.URL);

    def login(self, username: str, password: str) -> None:
            self.user_name.fill(username)
            self.password.fill(password)
            self.login_button.click()