from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class Test_Sauce_Valid_Login:
 def test_valid_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        assertLogin=driver.find_element(By.CLASS_NAME,"app_logo")
        sleep(2)
        print(f"login dogrulaması texti: {assertLogin.text}")
        resault=assertLogin.text=="Swag Labs"
        print(f"Test Sonucu: {resault}")
testClass=Test_Sauce_Valid_Login()
testClass.test_valid_login()