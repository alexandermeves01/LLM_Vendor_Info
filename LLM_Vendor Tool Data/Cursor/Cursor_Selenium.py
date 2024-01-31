from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_python_org_search():
    driver = webdriver.Firefox()  # or use webdriver.Chrome() if you prefer
    driver.get("https://www.python.org")

    assert "Welcome to Python.org" == driver.title

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys("getting started with python")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.python.org/search/?q=getting+started+with+python&submit=")
    )

    driver.quit()