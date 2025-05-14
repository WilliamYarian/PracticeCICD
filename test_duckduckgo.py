import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ✅ Fixture for WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# ✅ Test function using the fixture
def test_search_duckduckgo(driver):
    driver.get("https://duckduckgo.com/")
    time.sleep(1)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python course" + Keys.ENTER)

    time.sleep(2)
    assert "Python" in driver.title