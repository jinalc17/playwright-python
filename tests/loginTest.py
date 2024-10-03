from pages.login import LoginPage
from playwright.sync_api import Page, expect

def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user","secret_sauce")
    expect(page).to_have_title('Swag Labs')