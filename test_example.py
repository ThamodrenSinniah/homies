from selenium import webdriver


def test_example():
    browser = webdriver.Firefox()
    browser.get("http://selenium.dev/")
