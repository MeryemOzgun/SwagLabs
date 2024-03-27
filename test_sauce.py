from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait # ilgili driver ı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec # beklenen kousllar
from selenium.webdriver.common.action_chains import ActionChains # aksiyon zinciri 

class Test_Sauce:
    def __init__(self) -> None:
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        userNameInput=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID, "user-name")))
        passwordInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"1")
        actions.send_keys_to_element(passwordInput,"1")
        actions.perform()
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")))
        print(errorMessage.text)
        testResualt=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST invalid SONUCU: {testResualt}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        passwordInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        """ baslik =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        testResult = baslik.text == "Swag Labs" """
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        self.driver.execute_script("window.scrollTo(0,500)")
        addToCart.click()
        """ actions2 = ActionChains(self.driver)
        actions2.move_to_element(addToCart) #butonun olduğu yere sayfayı taşı
        actions2.click()
        actions2.perform() """
        removeButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")))
        testResult = removeButton.text == "Remove"
        sleep(3)
        print(f"TEST SONUCU: {testResult}")








testClass=Test_Sauce()
testClass.test_invalid_login()
sleep(2)
testClass.test_valid_login()