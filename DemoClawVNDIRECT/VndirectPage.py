

from DemoClawVNDIRECT.Browser import Browser



class VndirectPage(Browser):

    def __init__(self, pathdriver):
        super().__init__(pathdriver)
        self.eleUser = super().driver.Get("input[name='username']")
        self.elePassword =  super().driver.Get("input[name='password']")
        self.eleSubmit= super().driver.Get("//span[text()='Đăng nhập']/parent::*")

    def Login(self,user, password):
        self.eleUser.send_keys(user)
        self.elePassword.send_keys(password)
        self.eleSubmit.submit()