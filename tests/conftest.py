import logging
import os
import sys
import pytest
import pytest_html
from pytest_html import extras
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.app_settings import AppSettings
from wolt_pages.discovery_page import DiscoveryPage

def pytest_addoption(parser):
    """
    Adds a new command-line option --browser
    so you can run pytest like: pytest --browser=firefox
    """
    parser.addoption(
        "--browser_type",
        action="store",
        default="chromium",
        help="Browser to run tests, e.g. chromium, firefox, or webkit",
    )

@pytest.fixture(scope="function")
def browser_session(request):
    # Start Playwright
    with sync_playwright() as playwright:
        headless = AppSettings.is_headless()
        browser_args = AppSettings.get_browser_args()
        browser_type = request.config.getoption("--browser_type")

        if browser_type == "chromium":
            browser = playwright.chromium.launch(headless=headless, args=browser_args)
        elif browser_type == "firefox":
            browser = playwright.firefox.launch(headless=headless, args=browser_args)
        elif browser_type == "webkit":
            browser = playwright.webkit.launch(headless=headless, args=browser_args)
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")

        context = browser.new_context()
        page = context.new_page()
        page.goto(AppSettings.BASE_URL)
        yield page
        logging.info("Closing browser session...")
        context.close()
        browser.close()


# pytest hook for screenshots on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take a screenshot if a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page_fixture = item.funcargs.get("browser_session")
        if page_fixture:
            try:
                screenshot_dir = "screenshots/"
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = f"{screenshot_dir}/{item.name}.png"
                page_fixture.screenshot(path=screenshot_path)

                print(f"Screenshot saved to {screenshot_path}")
                # Attach the screenshot to the report
                if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                    extra = getattr(report, "extra", [])
                    extra.append(pytest_html.extras.image(screenshot_path))
                    report.extra = extra

            except Exception as e:
                logging.error(f"Failed to take screenshot: {e}")


@pytest.fixture(scope="function")
def discovery_page(browser_session):
    """Fixture to provide an instance of the DiscoveryPage."""
    return DiscoveryPage(browser_session)
