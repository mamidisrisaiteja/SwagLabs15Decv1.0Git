from playwright.sync_api import Page
import pytest
from playwright.sync_api import sync_playwright as p
from pages.login_page import LoginPage


# @pytest.fixture(scope="session")
# def browser(page: Page):
#     browser=p.chromium.launch(headed=False)
#     yield
#     browser.close()

# @pytest.fixture(scope="session") 
# def page(browser):
#     page_context=ge=browser.new_context()
#     page=page_context.new_page()
#     yield
#     page.close()

@pytest.fixture
def login_page(page,base_url):
    lp=LoginPage(page)
    base_url="https://www.saucedemo.com/"
    page.goto(base_url)
    return lp

# @pytest.fixture
# def login_page(page):
#     # 'page' here is the plugin's function-scoped fixture
#     return LoginPage(page)
