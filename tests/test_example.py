import pytest
from fixtures.browser import browser
from selenium.webdriver.common.by import By


def test_open_browser(browser: browser):
    browser.get("http://selenium.dev/")


@pytest.mark.parametrize("search_input", ["facebook", "twitter", "youtube"])
def test_search_google(browser: browser, search_input):
    browser.get("https://www.google.com/")
    search_bar = browser.find_element(By.XPATH, '//*[@title="Search"]')
    search_bar.send_keys(search_input)


# Todo
#   1. Do Assertions
#   2. Implicit waits
#   3. Sensitive test data hiding
