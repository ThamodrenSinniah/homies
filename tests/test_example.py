import os
import time

import pytest
from fixtures.browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from dotenv import load_dotenv


def test_open_browser(browser: browser):
    browser.get("http://selenium.dev/")


@pytest.mark.parametrize("search_input", ["facebook", "twitter", "youtube"])
def test_search_google(browser: browser, search_input):
    browser.get("https://www.google.com/")
    try:
        search_bar = browser.find_element(By.XPATH, '//*[@title="Thamo"]')
    except:
        search_bar = browser.find_element(By.XPATH, '//*[@title="Search"]')
    search_bar.send_keys(search_input)


def test_check_playwright_for_python(browser: browser):
    browser.get("https://playwright.dev/python/")
    title = browser.find_element(By.XPATH, '//*[@class="navbar__title text--truncate"]')
    assert title.text == "Playwright for Python"


def test_login(browser:browser):
    load_dotenv('.env')  # load my env variables
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    print(f'Printing email: {email}')
    print(f'Printing password: {password}')
    browser.get("https://e2e.vistasoftmonitor.com/")
    wait = WebDriverWait(browser, 15)

    email_input = wait.until(ec.visibility_of_element_located((By.ID, 'email')))
    password_input = wait.until(ec.visibility_of_element_located((By.ID, 'password')))

    email_input.send_keys(email)
    password_input.send_keys(password)

    browser.execute_script('''window.open("http://google.com","_blank");''')  # create new tab to google
    browser.switch_to.window(browser.window_handles[1])  # switch to second tab
    search_bar = browser.find_element(By.XPATH, '//*[@title="Search"]')  # search in google
    search_bar.send_keys("playboi carti")
    time.sleep(2)
    print(f'Printing without len(): {browser.window_handles}')
    print(f'Printing length: {len(browser.window_handles)}')
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()
    attribute_of_button = browser.find_element(By.ID, 'login-button').get_attribute("role")
    assert attribute_of_button == "button"

    assert wait.until(ec.visibility_of_element_located((By.XPATH, '//p[@title="s.thamodren@gmail.com"]')))


# Todo
#   1. Do Assertions
#   2. Implicit waits
#   3. Sensitive test data hiding

#  auto_xpath -> //*[@id="docusaurus_skipToContent_fallback"]/header/div/h1/span
#  xpath -> //span[contains(@class,'highlight')]


#  css   -> #docusaurus_skipToContent_fallback > header > div > h1 > span
