#coding=utf-8
from test.business.login_business import LoginBusiness
class LoginCase(object):
    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):
        LoginBusiness().Login(self.driver)

