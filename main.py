from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com.tr/")
sleep(3)
input= driver.find_element(By.NAME,"q")
input.send_keys("kodlama.io")
sleep(3)
#searchButton=driver.find_element(By.ID,"contents")
#searchButton.click
input.send_keys(Keys.RETURN)
sleep(3)
button=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
sleep(3)
button.click()
sleep(3)
curseList=driver.find_elements(By.CLASS_NAME,"course-listing")
sleep(3)
print("kurs sayisi=" +str(len(curseList)))