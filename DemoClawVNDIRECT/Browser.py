import time
from warnings import simplefilter
from numpy import int64
from pandas.core.algorithms import SelectNFrame
from pandas.io.pytables import SeriesFixed
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

    dct_FiRatios = {}
    lstAnual = []
    dct_Asset = {}

    def __init__(self, pathdriver):
        super().__init__(pathdriver)

    def eleSearchBox(self):
        return super().Get("#CafeF_SearchKeyword_Company")
    def eleSubmit(self):
        return super().Get(".s-submit")
    def eleBasicEPS(self):
        return super().Get("//a[contains(text(),'EPS cơ bản')]/following::div[1]")
    def eleDilutionEPS(self):
        return super().Get("//a[contains(text(),'EPS pha loãng')]/following::div[1]")

    @staticmethod
    def Getinfor(eleList,dict,KeyDict):
        temp = []
        for i in eleList:
            temp.append(i.text)
        dict[KeyDict] = temp
    
    # get list element and get multiple text
    def eleYears(self):
        return super().GetMutiple("//th[contains(text(),'Chỉ tiêu tài chính')]/following-sibling::*[@class='data']")
    def eleQuarter(self):
        return super().GetMutiple("//*[@id='divHoSoCongTyAjax']//th[position() > 1 and position() < 6]")
    def eleBasicEPSs(self):
        return super().GetMutiple("//label[contains(text(),'EPS')]/parent::*/following-sibling::*[not(@class='chart')]")
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
    
    #COMPANY ASSET
    def eleAsset(self):
        return super().GetMutiple("//*[contains(@id,'ctl01_rptData_ctl01_TrData')]/td[position()<6 and position()>1]")
    def eleShortAsset(self):
        return super().GetMutiple("//*[contains(@id,'ctl01_rptData_ctl00_TrData')]/td[position()<6 and position()>1]")
    def eleShortLiabilities(self):
        return super().GetMutiple("//*[contains(@id,'ctl01_rptData_ctl02_TrData')]/td[position()<6 and position()>1]")
    def eleTotalLiabilities(self):
        return super().GetMutiple("//*[contains(@id,'ctl01_rptData_ctl03_TrData')]/td[position()<6 and position()>1]")
    def eleOwnersEquity(self):
        return super().GetMutiple("//*[contains(@id,'ctl01_rptData_ctl04_TrData')]/td[position()<6 and position()>1]")

    def SearchByCode(self):
        #Code = str(input("Stock Code: "))
        time.sleep(1)
        self.eleSearchBox().send_keys("NKG")
        self.eleSubmit().click()    

    def GetFinancialRatios(self):
        self.Getinfor(self.eleDARs(),self.dct_FiRatios,"DAR")
        self.Getinfor(self.eleGOSs(),self.dct_FiRatios,"GOR")
        self.Getinfor(self.elePEs(),self.dct_FiRatios,"PE")
        self.Getinfor(self.eleBasicEPSs(),self.dct_FiRatios,"EPS")
        self.Getinfor(self.eleROSs(),self.dct_FiRatios,"ROS")
        self.Getinfor(self.eleROAs(),self.dct_FiRatios,"ROA")
        self.Getinfor(self.eleROEs(),self.dct_FiRatios,"ROE")
        for i in self.eleYears():
            self.lstAnual.append(i.text)

    def GetAsset(self):
        self.Getinfor(self.eleAsset(),self.dct_Asset,"Total Asset")
        self.Getinfor(self.eleShortAsset(),self.dct_Asset,"Short Current Asset")
        self.Getinfor(self.eleShortLiabilities(),self.dct_Asset,"Short Liabilities")
        self.Getinfor(self.eleTotalLiabilities(),self.dct_Asset,"Total Liabilities")
        self.Getinfor(self.eleOwnersEquity(),self.dct_Asset,"Owners’ equity")
        for i in self.eleQuarter():
            self.lstAnual.append(i.text)

    def CreateDF(self,dict):
        data = pd.DataFrame.from_dict(dict,orient='index',columns= self.lstAnual,dtype = float)
        df_percent = data.pct_change(axis='columns')        
        result = pd.concat([data,df_percent*100], axis= 1)
        self.lstAnual.clear()
        return result

    def FinancialRatios(self):
        self.GetFinancialRatios()        
        result = self.CreateDF(self.dct_FiRatios)
        print(result)

    def CompanyAsset(self):
        self.GetAsset()
        for k,v in self.dct_Asset.items():
            self.dct_Asset[k] = [i.replace(",","") for i in v ]/1000
        result = self.CreateDF(self.dct_Asset)
        print(result)

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
       