import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://phptravels.net/")

driver.find_element(By.ID, "ACCOUNT").click()
driver.find_element(By.LINK_TEXT,"Customer Login").click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("180040356ece@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Naveen@9390")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//a[@title='flights']").click()
driver.find_element(By.XPATH,"//label[@class='form-check-label']")
driver.find_element(By.CSS_SELECTOR,"input[id='autocomplete']").send_keys("BARODA")
driver.find_element(By.CSS_SELECTOR,"input[id='autocomplete2']").send_keys("Mysore Airport")
driver.find_element(By.CSS_SELECTOR,"input[id='departure']").send_keys("01-03-2023")
driver.find_element(By.XPATH,"//i[@class='la la-user form-icon']").click()
driver.find_element(By.XPATH,"//i[@class='la la-plus']").click()
driver.find_element(By.XPATH,"//i[@class='mdi mdi-search']").click()