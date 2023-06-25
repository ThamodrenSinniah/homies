import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    # Container does not have GPU so have to run on headless
    # Feel free to remove when testing locally to see the browser
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
