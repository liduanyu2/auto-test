#coding=utf-8
from test.base.find_element import FindElement
class LoginPage(object):
    def __init__(self,driver):
        self.fe=FindElement(driver)

    def get_username_element(self):
        return self.fe.get_element("userName")

    def get_password_element(self):
        return self.fe.get_element("passWord")

    def get_login_frame(self):
        return self.fe.get_element("frame")

    def get_login_button_element(self):
        return self.fe.get_element("login_bt")

    def get_login_submit_element(self):
        return self.fe.get_element("login_submit_bt")

    def get_code_element(self):
        return self.fe.get_element("code")