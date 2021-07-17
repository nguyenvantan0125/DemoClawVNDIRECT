from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 


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
    # GET MULTIPLE ELEMENT 
    def GetMutiple(self,element):
        if(element.startswith("//")):            
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, element)))
        else:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, element)))

class CafeF(Browser):

    # dctMetric = {
    #     "listROS" : [],
    #     "listROA" : [],
    #     "listROE" : [],
    #     "listGOS" : [],
    #     "listDAR" : [],
    #     "listPE" : []
    # }

    dctMetric = {}

    def __init__(self, pathdriver):
        super().__init__(pathdriver)

    def eleSearchBox(self):
        return super().Get("#CafeF_SearchKeyword_Company")
    def eleSubmit(self):
        return super().Get(".s-submit")
    def elePE(self):
        return super().Get("//b[contains(text(),'P/E')]/following::div[1]")
    def eleBasicEPS(self):
        return super().Get("//a[contains(text(),'EPS cơ bản')]/following::div[1]")
    def eleDilutionEPS(self):
        return super().Get("//a[contains(text(),'EPS pha loãng')]/following::div[1]")

    # get list element and get multiple text
    def elePEs(self):
        return super().GetMutiple("//label[contains(text(),'P/E')]/parent::*/following-sibling::*[not(@class='chart')]")
    def eleROAs(self):
        return super().GetMutiple("//label[contains(text(),'ROA')]/parent::*/following-sibling::*[not(@class='chart')]")
    def eleROEs(self):
        return super().GetMutiple("//label[contains(text(),'ROE')]/parent::*/following-sibling::*[not(@class='chart')]")
    def eleROSs(self):
        return super().GetMutiple("//label[contains(text(),'ROS')]/parent::*/following-sibling::*[not(@class='chart')]")
    def eleGOSs(self):
        return super().GetMutiple("//label[contains(text(),'GOS')]/parent::*/following-sibling::*[not(@class='chart')]")
    def eleDARs(self):
        return super().GetMutiple("//label[contains(text(),'DAR')]/parent::*/following-sibling::*[not(@class='chart')]")
    
    def SearchByCode(self):
        #Code = str(input("Stock cODE: "))
        self.eleSearchBox().send_keys("FPT")
        self.eleSubmit().click()    
    
    def GetListPE(self):
        listPE = self.elePEs
        for i in listPE:
            self.dctMetric["listPE"].append(i.text)

    def GetListROS(self):
        listelement = self.eleROAs()
        for i in listelement:
            self.dctMetric["listROS"].append(i.text)
    
    def GetListROA(self):
        listROS = self.eleROSs()
        for i in listROS:
            self.dctMetric["listROA"].append(i.text)
    
    def GetListROE(self):
        listROS = self.eleROEs()
        for i in listROS:
            self.dctMetric["listROE"].append(i.text)

    def GetListGOS(self):
        listGOS = self.eleGOSs()
        for i in listGOS:
            self.dctMetric["listGOS"].append(i.text)

    def GetListDAR(self):
        listDAR = self.eleDARs()
        for i in listDAR:
            self.dctMetric["listDAR"].append(i.text)

    def GetInfoDict(self):
        self.GetListDAR()
        self.GetListGOS()
        self.GetListPE()
        self.GetListROA()
        self.GetListROE()
        self.GetListROS()


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
       