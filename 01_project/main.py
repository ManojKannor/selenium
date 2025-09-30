from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

# Open Gmail login page
driver.get("https://accounts.google.com/signin")

# Store test cases
test_cases = [
    {"email": "validemail@gmail.com", "desc": "Valid email format"},
    {"email": "invalidemail", "desc": "Invalid email format (missing @)"},
    {"email": "invalid@gmail", "desc": "Invalid email format (missing .com)"},
    {"email": "", "desc": "Empty email field"},
    {"email": "test@example.com", "desc": "Non-Google email"}
]

for case in test_cases:
    print(f"\nRunning test case: {case['desc']}")

    # Locate email input
    email_input = driver.find_element(By.ID, "identifierId")
    email_input.clear()
    email_input.send_keys(case["email"])
    email_input.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for response

    try:
        # Check if error message is shown
        error = driver.find_element(By.XPATH, "//div[@class='o6cuMc']")
        print(f"Result: ❌ Error shown -> {error.text}")
    except:
        print("Result: ✅ No error (Google accepted input, moving to password step)")

    # Go back to login page for next test
    driver.get("https://accounts.google.com/signin")
    time.sleep(2)

driver.quit()
