from selenium import  webdriver
from selenium.webdriver.common.by import By

class Browser:
    def __init__(self, pathdriver): # khoi tao browser vs chrome driver
        self.driver = webdriver.Chrome(executable_path=pathdriver)

    def Loadpage(self, url): # Load page
        self.driver.get(url)

    def Get(self,element):
        if(element.startswith("//")):
            return self.driver.find_element(By.XPATH,element)
        else:
            return self.driver.find_element(By.CSS_SELECTOR,element)

    def tearDown(self):
        self.driver.quit()