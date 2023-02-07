import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FlightSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://phptravels.net/")

    def login(self):
        self.driver.find_element(By.ID, "ACCOUNT").click()
        self.driver.find_element(By.LINK_TEXT,"Customer Login").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("180040356ece@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Naveen@9390")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

    def search_flight(self):
        self.driver.find_element(By.XPATH,"//a[@title='flights']").click()
        self.driver.find_element(By.XPATH,"//label[@class='form-check-label']")
        self.driver.find_element(By.CSS_SELECTOR,"input[id='autocomplete']").send_keys("BARODA")
        self.driver.find_element(By.CSS_SELECTOR,"input[id='autocomplete2']").send_keys("Mysore Airport")
        self.driver.find_element(By.CSS_SELECTOR,"input[id='departure']").send_keys("09-02-2023")
        self.driver.find_element(By.XPATH,"//i[@class='la la-user form-icon']").click()
        self.driver.find_element(By.XPATH,"//i[@class='la la-plus']").click()
        self.driver.find_element(By.XPATH,"//i[@class='mdi mdi-search']").click()

class FlightSearchImpl(FlightSearch):
    def __init__(self):
        super().__init__()
        #self.open_website()
        self.login()
        self.search_flight()

    def ele(self):
        try:
            self.driver.find_element(By.ID, "ACCOUkgfsgs").click()
            print("Correct Xpath")
        except:
            print("Invalid xpath")

obj = FlightSearchImpl()
while True:
    print("Enter 1 for completion of process")
    print("Enter 2 to throw error")
    print("Enter 3 to quit")
    userchoice = int(input())
    if userchoice == 1:
        print("completion of process")
    elif userchoice == 2:
        obj.ele()
    elif userchoice == 3:
        quit()