import time
from selenium import  webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self, pathdriver): # khoi tao browser vs chrome driver
        self.driver = webdriver.Chrome(executable_path=pathdriver)        

    def Loadpage(self, url): # Load page
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
        
    def Get(self,element):
        if(element.startswith("//")):            
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))          
        else:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
           

class CafeF(Browser):
    def __init__(self, pathdriver):
        super().__init__(pathdriver)
    def eleSearchBox(self):
        return super().Get("#CafeF_SearchKeyword_Company")
    def eleSubmit(self):
        return super().Get(".s-submit")

    def SearchByCode(self,Code):        
        self.eleSearchBox().send_keys(Code)
        self.eleSubmit().click()
        
        


class VndirectPage(Browser):    
    
    def __init__(self, pathdriver):
        super().__init__(pathdriver)

    def eleUser(self):
        return super().Get("input[name='username']")
    def elePassword(self):
        return super().Get("input[name='password']")
    def eleSubmit(self):
        return super().Get("//span[text()='Đăng nhập']/parent::*")

    def Login(self,user, password):
        self.eleUser().send_keys(user)
        self.elePassword().send_keys(password)
       