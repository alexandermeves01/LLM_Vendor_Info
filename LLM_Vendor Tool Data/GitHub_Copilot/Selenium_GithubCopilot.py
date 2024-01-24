from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_webpage(driver, url):
    """
    Open a webpage using the provided webdriver and URL.

    Args:
        driver (webdriver): The webdriver instance to use.
        url (str): The URL of the webpage to open.
    """
    driver.get(url)
    assert driver.title == "Welcome to Python.org"

def search_python_org(driver, query):
    """
    Search python.org using the provided webdriver and query.

    Args:
        driver (webdriver): The webdriver instance to use.
        query (str): The search query.
    """
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    element.clear()
    element.send_keys(query)
    element.submit()

def verify_search(driver, query):
    """
    Verify the search results on python.org using the provided webdriver and query.

    Args:
        driver (webdriver): The webdriver instance to use.
        query (str): The search query.
    """
    expected_url = f"https://www.python.org/search/?q={query.replace(' ', '+')}&submit="
    assert driver.current_url == expected_url

def main():
    """
    Main function to open python.org, perform a search, and verify the search results.
    """
    with webdriver.Chrome() as driver:
        try:
            open_webpage(driver, "https://www.python.org/")
            search_python_org(driver, "getting started with python")
            verify_search(driver, "getting started with python")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
