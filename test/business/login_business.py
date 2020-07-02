#coding=utf-8
from test.handle.login_handle import LoginHandle
import time
from test.page.login_page import LoginPage
from test.base.read_image import ReadImage

class LoginBusiness(object):
    def __init__(self,driver):
        self.login_h=LoginHandle(driver)
        self.d1=driver

    def login_base(self,username=None,password=None,code=None):
        self.login_h.click_login_button()
        time.sleep(1)
        self.login_h.to_login_frame()
        self.login_h.input_username(username)
        self.login_h.input_password(password)
        time.sleep(1)
        if LoginPage(self.d1).get_code_element().is_displayed() != False:
            if code==None:
                self.code1=ReadImage().read_code(self.d1)
                self.login_h.input_code(self.code1)
            else:
                self.login_h.input_code(code)
        else:
            pass
        self.login_h.click_login_summit_button()
