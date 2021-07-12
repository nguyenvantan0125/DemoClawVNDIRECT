from Browser import *

Vnpage = CafeF(r'D:\VNDIRECT\DemoClawVNDIRECT\chromedriver.exe')
Vnpage.Loadpage("https://cafef.vn/")
#Vnpage.Loadpage("https://trade.vndirect.com.vn/chung-khoan/vn30")

Vnpage.SearchByCode("fpt")
#Vnpage.Login("nguyenvantan","Vantan@252525")

# Vnpage.tearDown()

