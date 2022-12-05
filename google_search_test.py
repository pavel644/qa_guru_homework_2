import pytest
from selene.support.shared import browser
from selene import be, have
import pytest


# настраиваем браузер, выбираем разрешение
@pytest.fixture()
def open_browser():
    browser.config.window_height = 768
    browser.config.window_width = 1024
    browser.open('https://google.com')

def test_find_selene_in_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('selene: User-oriented Web UI browser tests in Python'))

def test_do_not_find_nonsense_in_google(open_browser):
    nonsense_string = 'PIJN089uwe0243rlvksjBIUEDYfsd'
    browser.element('[name="q"]').should(be.blank).type(nonsense_string).press_enter()
    browser.element('[id="res"]').should(have.text('ничего не найдено'))