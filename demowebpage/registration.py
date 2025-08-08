from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time


test_cases = [
    {"id": "TC_REG_01", "gender": "Male", "fname": "John", "lname": "Doe", "email": "john.test001@example.com", "pwd": "Password123", "cpwd": "Password123"},
    {"id": "TC_REG_02", "gender": "", "fname": "", "lname": "", "email": "", "pwd": "", "cpwd": ""},
    {"id": "TC_REG_03", "gender": "Male", "fname": "John", "lname": "Doe", "email": "invalidemail@", "pwd": "Password123", "cpwd": "Password123"},
    {"id": "TC_REG_04", "gender": "Male", "fname": "John", "lname": "Doe", "email": "john.test004@example.com", "pwd": "Password123", "cpwd": "Password321"},
    {"id": "TC_REG_05", "gender": "Male", "fname": "John", "lname": "Doe", "email": "john.test005@example.com", "pwd": "123", "cpwd": "123"},
    {"id": "TC_REG_06", "gender": "Male", "fname": "John", "lname": "Doe", "email": "alreadyused@example.com", "pwd": "Password123", "cpwd": "Password123"},
    {"id": "TC_REG_07", "gender": "Male", "fname": "", "lname": "Doe", "email": "john.test007@example.com", "pwd": "Password123", "cpwd": "Password123"},
    {"id": "TC_REG_08", "gender": "", "fname": "John", "lname": "Doe", "email": "john.test008@example.com", "pwd": "Password123", "cpwd": "Password123"},
    {"id": "TC_REG_09", "gender": "Male", "fname": "John", "lname": "Doe", "email": "john.test009@example.com", "pwd": "", "cpwd": "Password123"},
    {"id": "TC_REG_10", "gender": "Male", "fname": "John", "lname": "Doe", "email": "john.test010@example.com", "pwd": "Password123", "cpwd": ""},
]


driver = webdriver.Chrome()

def fill_form(case):
    driver.get("https://demowebshop.tricentis.com/register")
    time.sleep(1)

    print(f"Running {case['id']}")

    
    if case["gender"] == "Male":
        driver.find_element(By.ID, "gender-male").click()
    elif case["gender"] == "Female":
        driver.find_element(By.ID, "gender-female").click()

 
    driver.find_element(By.ID, "FirstName").send_keys(case["fname"])
    driver.find_element(By.ID, "LastName").send_keys(case["lname"])
    driver.find_element(By.ID, "Email").send_keys(case["email"])
    driver.find_element(By.ID, "Password").send_keys(case["pwd"])
    driver.find_element(By.ID, "ConfirmPassword").send_keys(case["cpwd"])

   
    driver.find_element(By.ID, "register-button").click()
    time.sleep(2)

    
    try:
        result_text = driver.find_element(By.CLASS_NAME, "result").text
        print(f"{case['id']} Result: {result_text}")
    except:
        errors = driver.find_elements(By.CLASS_NAME, "field-validation-error")
        if errors:
            for err in errors:
                print(f"{case['id']} Error: {err.text}")
        else:
            summary = driver.find_elements(By.CLASS_NAME, "message-error")
            for s in summary:
                print(f"{case['id']} Error: {s.text}")
    print("-" * 60)
    time.sleep(2)


for case in test_cases:
    fill_form(case)

driver.quit()
