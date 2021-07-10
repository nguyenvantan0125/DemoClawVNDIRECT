from selenium import  webdriver
from Browser import *

driver = Browser(r'D:\VNDIRECT\DemoClawVNDIRECT\chromedriver.exe')
driver.Loadpage("https://trade.vndirect.com.vn/chung-khoan/vn30")


eleUser = driver.Get("input[name='username']")
elePassword =  driver.Get("input[name='password']")
eleSubmit= driver.Get("//span[text()='Đăng nhập']/parent::*")

def Login(user, password):
    eleUser.send_keys(user)
    elePassword.send_keys(password)
    eleSubmit.submit()

Login("nguyenvantan0125","Vantan@252525")
el = driver.Get("#TPBbP3")
print(el.text)
#driver.Quit()
