from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def check_python_org():
    # Open Chrome browser
    driver = webdriver.Chrome()
    # Open the web page
    driver.get("https://www.python.org")
    # Check if the title of the page contains "Welcome to Python.org"
    assert "Welcome to Python.org" in driver.title
    # Find the input element with the name "q" and clear its contents
    element = driver.find_element_by_name("q")
    element.clear()
    # Send the keys "getting started with python" to the cleared element
    element.send_keys("getting started with python")
    # Simulate pressing the Enter key
    element.send_keys(Keys.RETURN)
    # Check if the current URL matches the expected URL
    assert driver.current_url == "https://www.python.org/search/?q=python&submit="
    # Close the browser
    driver.close()

check_python_org()