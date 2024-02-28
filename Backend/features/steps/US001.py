from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function to initialize WebDriver
def init_webdriver():
    chrome_options = Options()
    # Uncomment for headless mode
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=chrome_options)

@given("the visitor is on the NutriPapi account creation page")
def step_impl(context):
    context.driver = init_webdriver()
    context.driver.get("http://localhost:3000/signup")

@when("they submit their personal details along with a chosen username and password")
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("newuser")
    context.driver.find_element(By.ID, "email").send_keys("newuser@example.com")
    context.driver.find_element(By.ID, "password").send_keys("securepassword123")
    context.driver.find_element(By.ID, "submit").click()

@then("their user account is created, and they are logged into the NutriPapi system")
def step_impl(context):
    assert "Welcome, newuser" in context.driver.page_source
    context.driver.quit()

@when("they attempt to create an account using an email address that is already associated with an existing account")
def step_impl(context):
    context.driver.find_element(By.ID, "email").send_keys("existinguser@example.com")
    context.driver.find_element(By.ID, "submit").click()

@then('a "Email already in use" error message is displayed')
def step_impl(context):
    assert "Email already in use" in context.driver.page_source
    context.driver.quit()

@when("they attempt to submit the account creation form without filling out all mandatory fields")
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()

@then('an "All fields are required" error message is displayed')
def step_impl(context):
    assert "All fields are required" in context.driver.page_source
    context.driver.quit()
