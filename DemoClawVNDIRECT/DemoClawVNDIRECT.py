from VndirectPage import *

Vnpage = VndirectPage(r'D:\VNDIRECT\DemoClawVNDIRECT\chromedriver.exe')
Vnpage.Loadpage("https://trade.vndirect.com.vn/chung-khoan/vn30")

Vnpage.Login("nguyenvantan0125","Vantan@252525")

Vnpage.tearDown()

