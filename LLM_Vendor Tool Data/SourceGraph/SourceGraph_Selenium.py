#Use Selenium to assert the title of the webpage "https://www..python.org" is "Welcome to Python". Find the webpage element with the name "q",
#clear the element, send keys "getting started with Python" and then submit. Assert the driver's current url is equal to 
#'https://www.python.org/search/?q=getting+started+with+python'

from selenium import webdriver
import unittest

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertEqual(driver.title, "Welcome to Python.org")
        
        search_box = driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys("getting started with Python")
        search_box.submit()
        
        self.assertEqual(driver.current_url, "https://www.python.org/search/?q=getting+started+with+python")
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

#Use Selenium to submit "standard_user" in the element "user-name", "secret_sauce" in the element 'password' and click the 'login-button'. Then sleep for 5

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")  
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(5) # sleep for 5 seconds

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/") 

# Login 
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Click 3 items
buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for i in range(3):
    buttons[i].click()

# Verify cart count    
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert cart_badge.text == "3"

# Click 2 more items
buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory") 
for i in range(2):
    buttons[i].click()
    
# Verify updated count
assert cart_badge.text == "1"  

driver.quit()
