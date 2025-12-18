
# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader  # adjust import path to your project


# -------- Config fixtures --------

@pytest.fixture(scope="session")
def app_config():
    """Load app config once per test session."""
    return ConfigReader("config.yml").load_config()  # reads config.yml by default


@pytest.fixture(scope="session")
def browser_type(app_config):
    """Return the browser type: chromium/firefox/webkit."""
    name = (app_config.get("browser") or "chromium").lower()
    if name not in {"chromium", "firefox", "webkit"}:
        raise ValueError(f"Unsupported browser in config: {name}")
    return name


@pytest.fixture(scope="session")
def headless(app_config):
    """Return headless boolean from config (supports 'headless' or 'headLess')."""
    raw = app_config.get("headless", app_config.get("headLess", True))
    if isinstance(raw, str):  # normalize string values like "true"/"false"
        return raw.strip().lower() in {"1", "true", "yes", "on"}
    return bool(raw)


@pytest.fixture(scope="session")
def base_url(app_config):
    """Return base URL from config."""
    return app_config.get("base_url", "https://www.saucedemo.com/")


# -------- Playwright lifecycle fixtures --------

@pytest.fixture(scope="session")
def playwright():
    """Start Playwright for the session."""
    with sync_playwright() as pw:
        yield pw
    # auto-closed by the context manager


@pytest.fixture(scope="session")
def browser(playwright, browser_type, headless):
    """Launch the chosen browser with headless flag."""
    launchers = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }
    browser_launcher = launchers[browser_type]
    browser = browser_launcher.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """Create a new context per test (isolated cookies/storage)."""
    ctx = browser.new_context()
    yield ctx
    ctx.close()


@pytest.fixture(scope="function")
def page(context, base_url):
    """Provide a ready-to-use page and navigate to base_url."""
    pg = context.new_page()
    if base_url:
        pg.goto(base_url)
    yield pg
    pg.close()


# -------- Page Object fixtures --------

@pytest.fixture(scope="function")
def login_page(page):
    """Return LoginPage; 'page' is already at base_url."""
    return LoginPage(page)
