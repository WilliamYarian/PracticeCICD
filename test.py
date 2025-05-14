from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_duckduckgo_search():
    # 👇 Replace this path with the actual one if different
    driver = webdriver.Chrome()

    driver.get("https://duckduckgo.com/")
    time.sleep(1)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python course" + Keys.ENTER)

    time.sleep(2)
    assert "Python" in driver.title

    driver.quit()
