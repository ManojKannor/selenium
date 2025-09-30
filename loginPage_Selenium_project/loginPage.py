from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver= driver
        self.username_field = (By.ID,'MainContent_TBUserName')
        self.password_field = (By.ID,'MainContent_TBPassword')
        self.LoginBtn = (By.XPATH, '//*[@id="MainContent_BtnLogin"]')

        self.invalid_creds = (By.XPATH,'//*[@id="MainContent_DivToastAlert"]')
    
    def enter_username(self,username):
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.LoginBtn)

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
