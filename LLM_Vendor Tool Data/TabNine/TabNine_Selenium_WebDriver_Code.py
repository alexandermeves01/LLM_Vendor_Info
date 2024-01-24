from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_python_org_title(driver):
    # Open the Python website
    driver.get("https://www.python.org")

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Python"))

    # Check if the title is correct
    title = driver.title
    if title != "Welcome to Python.org":
        raise ValueError(f"Expected title 'Welcome to Python.org', got '{title}'")

    # Clear the search box
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()

    # Enter the search query
    search_box.send_keys("getting started with python")

    # Submit the search
    search_box.submit()

    # Wait for the page to load
    wait.until(EC.url_to_be("https://www.python.org/search/?q={getting+started+with+python}&submit="))

    # Check if the URL is correct
    url = driver.current_url
    if url != "https://www.python.org/search/?q={getting+started+with+python}&submit=":
        raise ValueError(f"Expected URL 'https://www.python.org/search/?q={getting+started+with+python}&submit='")

if __name__ == "__main__":
    # Start the browser
    driver = webdriver.Chrome()

    # Run the tests
    try:
        check_python_org_title(driver)
        print("Success!")
    except Exception as e:
        print(f"Failed: {e}")

    # Close the browser
    driver.close()