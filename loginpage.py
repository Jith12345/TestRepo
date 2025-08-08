from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
base_url = 'https://demowebshop.tricentis.com/login'

def login_test(email, password, expected_text):
    driver.get(base_url)
    time.sleep(1)
    driver.find_element(By.ID, 'Email').clear()
    driver.find_element(By.ID, 'Email').send_keys(email)
    driver.find_element(By.ID, 'Password').clear()
    driver.find_element(By.ID, 'Password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input.login-button').click()
    time.sleep(2)
    if expected_text.lower() in driver.page_source.lower():
        print(f' Test Passed for Email: {email}')
    else:
        print(f' Test Failed for Email: {email} - Expected: {expected_text}')


login_test('testjith5@gmail.com', 'test123', 'User should be logged in successfully')
driver.find_element(By.CLASS_NAME, 'ico-logout').click()

login_test('user@example.com', 'wrong123', "Invalid login credentials")
login_test('user@com', 'Test@123', 'email format validation error')
login_test('', 'Test@123', 'Email is required')
login_test('user@example.com', '', 'Password is required')

time.sleep(3)
driver.quit()


    