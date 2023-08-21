from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils import json_reader

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    login_menu = (By.ID, 'login2')    
    username_input = (By.ID, 'loginusername')
    password_input = (By.ID, 'loginpassword')
    login_button = (By.XPATH, "//button[normalize-space()='Log in']")

    def enter_credentials(self):
        datos = json_reader.read_json('data.json')
        username = datos['username']
        password = datos['password']

        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()