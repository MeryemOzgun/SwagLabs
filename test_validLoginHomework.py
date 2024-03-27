from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl


class Test_ValidLoginHomework:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def teardown_method(self):
        self.driver.quit()

    def getDataFromExcel(self):
        wb = openpyxl.load_workbook("C:\\Users\\my\\Desktop\\seleniumProje\\data\\veriler.xlsx")
        sheet = wb.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            username = row[0]
            password = row[1]
            data.append((username, password))
        return data

    @pytest.mark.parametrize("username, password", self.getDataFromExcel())
    def test_valid_login(self, username, password):
        userNameInput = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        passwordInput = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        baslik = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")))
        assert baslik.text == "Swag Labs"