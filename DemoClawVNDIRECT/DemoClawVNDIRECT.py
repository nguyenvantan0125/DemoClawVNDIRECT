from selenium import  webdriver
import time

driver = webdriver.Chrome(executable_path =r'D:\VNDIRECT\DemoClawVNDIRECT\chromedriver.exe' )
driver.get("https://www.google.com/")

print(driver.title)
el = driver.find_element_by_name("q")
el.send_keys("Hinh hoc")
el.submit()
driver.quit()
