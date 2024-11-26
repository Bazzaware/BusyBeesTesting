from selenium import webdriver
from selenium.webdriver.common.by import By


def setup():
    driver = webdriver.Chrome()
    driver.get("https://busybeesrecipes.azurewebsites.net")
    return driver


def test_front_page():
    driver = setup()

    title = driver.title

    assert title == "Busybees Recipes"
    driver.implicitly_wait(0.5)

    login_button = driver.find_element(by=By.CLASS_NAME, value="custom-btn-orange.btn")
    assert login_button.text == "Sign In"

    register_button = driver.find_element(
        by=By.CLASS_NAME, value="custom-btn-no-fill.btn"
    )
    assert register_button.text == "Register"

    teardown(driver)


def test_login():
    driver = setup()

    login_button = driver.find_element(by=By.CLASS_NAME, value="custom-btn-orange.btn")
    login_button.click()

    user_name_input = driver.find_element(by=By.ID, value="formBasicUsername")
    assert user_name_input.get_attribute("placeholder") == "Username"

    password_input = driver.find_element(by=By.ID, value="formBasicPassword")
    assert password_input.get_attribute("placeholder") == "Password"


def teardown(driver):
    driver.quit()
