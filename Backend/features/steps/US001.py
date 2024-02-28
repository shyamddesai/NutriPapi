from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Assuming use of Chrome; adjust based on your browser and setup
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

@given("the visitor is on the NutriPapi account creation page")
def step_impl(context):
    driver.get("http://localhost:3000/signup")

@when("they submit their personal details along with a chosen username and password")
def step_impl(context):
    # Example; adjust field IDs as necessary
    driver.find_element_by_id("username").send_keys("newuser")
    driver.find_element_by_id("email").send_keys("newuser@example.com")
    driver.find_element_by_id("password").send_keys("securepassword123")
    driver.find_element_by_id("submit").click()

@then("their user account is created, and they are logged into the NutriPapi system")
def step_impl(context):
    assert "Welcome, newuser" in driver.page_source

@when("they attempt to create an account using an email address that is already associated with an existing account")
def step_impl(context):
    driver.find_element_by_id("email").send_keys("existinguser@example.com")
    driver.find_element_by_id("submit").click()

@then('a "Email already in use" error message is displayed')
def step_impl(context):
    assert "Email already in use" in driver.page_source

@when("they attempt to submit the account creation form without filling out all mandatory fields")
def step_impl(context):
    driver.find_element_by_id("submit").click()

@then('an "All fields are required" error message is displayed')
def step_impl(context):
    assert "All fields are required" in driver.page_source

