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


class Locator:
    eleUser = "input[name='username']"
    elePassword =  "input[name='password']"
    eleSubmit= "//span[text()='Đăng nhập']/parent::*"

    def Get(self,element):
        if(element.startswith("//")):
            return self.driver.find_element(By.XPATH,element)
        else:
            return self.driver.find_element(By.CSS_SELECTOR,element) 

class VndirectPage(Browser,Locator):    

    def __init__(self, pathdriver):
        super(Browser).__init__(pathdriver)


    def Login(self,user, password):
        Locator.Get(Locator.eleUser).send_keys(user)
        Locator.Get(Locator.eleUser).send_keys(password)
       