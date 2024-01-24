from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def check_title_and_search():
    driver = webdriver.Chrome() # or you can use Chrome()

    # Open the website
    driver.get("https://www.python.org")

    # Check the title
    assert "Welcome to Python.org" in driver.title

    # Find the element with the name "q"
    elem = driver.find_element_by_name("q")

    # Clear it
    elem.clear()

    # Send keys
    elem.send_keys("getting started with python")

    # Submit the form
    elem.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(2)

    # Check the URL
    assert driver.current_url == "https://www.python.org/search/?q=getting+started+with+python"

    # Close the browser
    driver.quit()

check_title_and_search()    