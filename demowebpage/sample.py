from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Test Data for test cases
test_cases = [
    {"TC_ID": "TC001", "gender": "Male", "first_name": "John", "last_name": "Doe", "email": "john.doe123@test.com", "password": "Test@1234", "confirm_password": "Test@1234"},
    {"TC_ID": "TC002", "gender": "Male", "first_name": "John", "last_name": "Doe", "email": "john.doe124@test.com", "password": "Test@1234", "confirm_password": "Test@1234"},
    {"TC_ID": "TC003", "gender": "Male", "first_name": "John", "last_name": "Doe", "email": "john.doe.com", "password": "Test@1234", "confirm_password": "Test@1234"},
    {"TC_ID": "TC004", "gender": "Male", "first_name": "John", "last_name": "Doe", "email": "john.diff123@test.com", "password": "Test@1234", "confirm_password": "Test@5678"},
    {"TC_ID": "TC005", "gender": "", "first_name": "Jane", "last_name": "Doe", "email": "jane.doe123@test.com", "password": "Test@1234", "confirm_password": "Test@1234"},
    {"TC_ID": "TC006", "gender": "Male", "first_name": "", "last_name": "", "email": "", "password": "", "confirm_password": ""},
    {"TC_ID": "TC007", "gender": "Male", "first_name": "Tom", "last_name": "Jerry", "email": "tom.jerry@test.com", "password": "12345", "confirm_password": "12345"},
    {"TC_ID": "TC008", "gender": "Male", "first_name": "John", "last_name": "Doe", "email": "JOHN.DOE123@test.com", "password": "Test@1234", "confirm_password": "Test@1234"},
    {"TC_ID": "TC010", "gender": "Male", "first_name": "@John", "last_name": "Doe", "email": "john.special@test.com", "password": "Test@1234", "confirm_password": "Test@1234"},
]

# Set up Chrome WebDriver (browser will be visible)
options = Options()
# options.add_argument("--headless")  # Uncomment this line if you want headless mode
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def register_user(test_data):
    driver.get("https://demowebshop.tricentis.com/register")
    time.sleep(1)
    
    # Gender
    if test_data["gender"] == "Male":
        driver.find_element(By.ID, "gender-male").click()
    elif test_data["gender"] == "Female":
        driver.find_element(By.ID, "gender-female").click()
        
    driver.find_element(By.ID, "FirstName").clear()
    driver.find_element(By.ID, "FirstName").send_keys(test_data["first_name"])
    
    driver.find_element(By.ID, "LastName").clear()
    driver.find_element(By.ID, "LastName").send_keys(test_data["last_name"])
    
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Email").send_keys(test_data["email"])
    
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys(test_data["password"])
    
    driver.find_element(By.ID, "ConfirmPassword").clear()
    driver.find_element(By.ID, "ConfirmPassword").send_keys(test_data["confirm_password"])
    
    driver.find_element(By.ID, "register-button").click()
    
    time.sleep(2)
    try:
        # Check for success message
        success = driver.find_elements(By.CLASS_NAME, "result")
        if success and "Your registration completed" in success[0].text:
            print(f"{test_data['TC_ID']}: Passed - Registration successful")
            # Log out for next test case
            try:
                driver.find_element(By.CLASS_NAME, "ico-logout").click()
            except:
                pass
            return
    except Exception:
        pass

    try:
        # Check for validation summary errors
        error_box = driver.find_element(By.CLASS_NAME, "message-error")
        print(f"{test_data['TC_ID']}: Failed - {error_box.text.strip()}")
    except:
        print(f"{test_data['TC_ID']}: Failed - Validation or unexpected error occurred")

# Execute each test case
for tc in test_cases:
    register_user(tc)

driver.quit()