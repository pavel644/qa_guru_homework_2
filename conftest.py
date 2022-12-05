import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_browser_resolution():
    browser.config.window_height = 768
    browser.config.window_width = 1024


@pytest.fixture()
def open_browser(set_browser_resolution):
    browser.open('https://google.com')
