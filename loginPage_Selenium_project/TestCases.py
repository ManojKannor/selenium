import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from loginPage import LoginPage

@pytest.fixture(scope="function")
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://erp.metbhujbalknowledgecity.ac.in/StudLogin.aspx")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver=setup
    login_page1 = LoginPage(driver)
    login_page1.login("N04032300033","N0403230003")
    # assert "Dashboard" in driver.title, "Valid login failed!"

def test_invalid_login(setup):
    driver=setup
    login_page1 = LoginPage(driver)
    login_page1.login("32343232333","3342323434")