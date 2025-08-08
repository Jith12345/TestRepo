from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the login page
driver.get("https://demowebshop.tricentis.com/login")
time.sleep(2)

# Input login credentials
email = "testjith5@gmail.com"
password = "test123"

driver.find_element(By.ID, "Email").send_keys(email)
driver.find_element(By.ID, "Password").send_keys(password)

# Click login button
driver.find_element(By.CSS_SELECTOR, "input.login-button").click()
time.sleep(3)

# Validation
if "Log out" in driver.page_source:
    print("Login successful")
else:
    print("Login failed")

driver.find_element(By.CSS_SELECTOR, "input.button-2.product-box-add-to-cart-button").click()
time.sleep(3)

RecipientName = "John Doe"
RecipientEmail = "testjith5@gmail.com"
driver.find_element(By.ID,"giftcard_2_RecipientName").send_keys(RecipientName)
driver.find_element(By.ID,"giftcard_2_RecipientEmail").send_keys(RecipientEmail)

driver.find_element(By.CLASS_NAME, "ico-cart").click()

try:
    checkbox = driver.find_element(By.ID, "termsofservice")
    if not checkbox.is_selected():
        checkbox.click()
except Exception as e:
    print("Error handling the terms of service checkbox:", e)

driver.find_element(By.ID, "checkout").click()

#billing address
continue_button = driver.find_element(By.CSS_SELECTOR, "input.button-1.new-address-next-step-button")
continue_button.click()

#shipping address
new_address_continue = driver.find_element(
    By.XPATH, "//input[@class='button-1 new-address-next-step-button']")
new_address_continue.click()
print("Shipping address continue button found")

# 3. Continue on Shipping Method
driver.find_element(By.CSS_SELECTOR, "input.button-1.shipping-method-next-step-button").click()
print("Shipping method step completed")
time.sleep(5)

# 4. Continue on Payment Method (default or previously selected)
driver.find_element(By.CSS_SELECTOR, "input.button-1.payment-method-next-step-button").click()
print(" Payment method step completed")
time.sleep(5)

# 5. Continue on Payment Info
driver.find_element(By.CSS_SELECTOR, "input.button-1.payment-info-next-step-button").click()
print(" Payment info step completed")
time.sleep(5)

# 6. Confirm Order
driver.find_element(By.CSS_SELECTOR, "input.button-1.confirm-order-next-step-button").click()
print("Order confirmed")
time.sleep(3)

# 7. Click Order Details
driver.find_element(By.LINK_TEXT, "Click here for order details.").click()
print(" Navigated to order details")


time.sleep(30)


