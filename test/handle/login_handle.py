#coding=utf-8
from test.page.login_page import LoginPage
class LoginHandle(object):
    def __init__(self,driver):
        self.login_p=LoginPage(driver)

    def send_username(self,username):
        self.login_p.get_username_element().send_keys(username)