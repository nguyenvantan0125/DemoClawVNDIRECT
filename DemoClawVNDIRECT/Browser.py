from selenium import  webdriver
from selenium.webdriver.common.by import By

class Browser:
    def __init__(self, pathdriver): # khoi tao browser vs chrome driver
        self.driver = webdriver.Chrome(executable_path=pathdriver)

    def Loadpage(self, url): # Load page
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()


class Locator:
    def eleUser(self):
        return self.Get("input[name='username']")
    def elePassword(self):
        return self.Get("input[name='password']")
    def eleSubmit(self):
        return self.Get("//span[text()='Đăng nhập']/parent::*")

    def Get(self,element):
        if(element.startswith("//")):
            return self.driver.find_element(By.XPATH,element)
        else:
            return self.driver.find_element(By.CSS_SELECTOR,element) 

class VndirectPage(Browser,Locator):

    def __init__(self, pathdriver):
        super().__init__(self,pathdriver)

    def Login(self,user, password):
        Locator.eleUser(self).send_keys(user)
        Locator.elePassword(self).send_keys(password)
       