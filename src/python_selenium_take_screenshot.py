from selenium import webdriver

URL = "https://wikipedia.org"

SCREENSHOT = "screenshot.png"

driver = webdriver.Firefox()

driver.get(URL)

driver.save_screenshot(SCREENSHOT)
