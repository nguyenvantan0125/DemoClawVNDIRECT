from selenium import  webdriver

driver = webdriver.Chrome(executable_path =r'D:\VNDIRECT\DemoClawVNDIRECT\chromedriver.exe' )
driver.get("https://trade.vndirect.com.vn/chung-khoan/vn30")

eleUser = driver.find_element_by_css_selector("input[name='username']")
elePassword =  driver.find_element_by_css_selector("input[name='password']")
eleSubmit= driver.find_element_by_xpath("//span[text()='Đăng nhập']/parent::*")

def Login(user, password):
    eleUser.send_keys(user)
    elePassword.send_keys(password)
    eleSubmit.submit()

Login("nguyenvantan0125","Vantan@252525")
print(driver.title)
el = driver.find_element_by_css_selector("#TPBbP3")
print(el.text)
el.click
el.click

driver.quit()
