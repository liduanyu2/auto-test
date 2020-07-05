#coding=utf-8
from test.page.login_page import LoginPage
from test.base.set_frame import SetFrame
from test.base.find_element import FindElement
class LoginHandle(object):
    def __init__(self,driver):
        self.login_p=LoginPage(driver)
        self.frame=driver

    def click_login_button(self):
        self.login_p.get_login_button_element().click()

    def input_username(self,username):
        self.login_p.get_username_element().send_keys(username)

    def input_password(self,password):
        self.login_p.get_password_element().send_keys(password)

    def input_code(self,code):
        self.login_p.get_code_element().send_keys(code)

    def to_login_frame(self):
        SetFrame(self.frame).to_frame("frame")

    def click_login_submit_button(self):
        self.login_p.get_login_submit_element().click()