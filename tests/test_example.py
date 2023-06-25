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
    #  An example of error handling
    #  Try to find a search bar called Thamo, if i cant find it, find a search bar called Search
    try:
        search_bar = browser.find_element(By.XPATH, '//*[@title="Thamo"]')
    except:
        search_bar = browser.find_element(By.XPATH, '//*[@title="Search"]')
    search_bar.send_keys(search_input)


def test_check_playwright_for_python(browser: browser):
    browser.get("https://playwright.dev/python/")
    title = browser.find_element(By.XPATH, '//*[@class="navbar__title text--truncate"]')
    # Assertion example
    # I want to assert that the text of the title ios the correct sentence
    assert title.text == "Playwright for Python"

# This test for some reason is failing on the container because it is not getting the environment variables
# Not sure why so ignore ig this fails on the container
def test_login(browser: browser):
    # Example of Hiding sensitive data
    # I added the variables on a file called .env
    # So everyone would know the variable is EMAIL and PASSWORD, but no one knows the actual values of the variables
    load_dotenv('.env')  # load my env variables
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    print(f'Printing email: {email}')
    print(f'Printing password: {password}')


    browser.get("https://e2e.vistasoftmonitor.com/")
    wait = WebDriverWait(browser, 15)

    # Example of waiting
    # I wait until the email and password field is visible
    email_input = wait.until(ec.visibility_of_element_located((By.ID, 'email')))
    password_input = wait.until(ec.visibility_of_element_located((By.ID, 'password')))

    email_input.send_keys(email)
    password_input.send_keys(password)

    # Creating a new tab that goes to google
    browser.execute_script('''window.open("http://google.com","_blank");''')
    # switch to the second tab (First tab is [0], second tab is [1]. Cus its an array/list)
    browser.switch_to.window(browser.window_handles[1])

    search_bar = browser.find_element(By.XPATH, '//*[@title="Search"]')
    search_bar.send_keys("playboi carti")
    time.sleep(2)

    # Getting the total amount of tabs opened
    print(f'Printing length: {len(browser.window_handles)}')

    # This closes the tab. NOT the whole browser. That is browser.quit
    browser.close()

    # I switch back to the first tab, because my focus will still be on the second tab if i did not switch back
    browser.switch_to.window(browser.window_handles[0])

    login_button = browser.find_element(By.ID, 'login-button')
    login_button.click()
    attribute_of_button = browser.find_element(By.ID, 'login-button').get_attribute("role")
    # More examples of assertions
    assert attribute_of_button == "button"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, '//p[@title="s.thamodren@gmail.com"]')))

#  auto_xpath -> //*[@id="docusaurus_skipToContent_fallback"]/header/div/h1/span
#  xpath -> //span[contains(@class,'highlight')]
#  css   -> #docusaurus_skipToContent_fallback > header > div > h1 > span
