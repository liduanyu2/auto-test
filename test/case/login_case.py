#coding=utf-8
from test.business.login_business import LoginBusiness
import time
class LoginCase(object):
    def __init__(self,driver):
        self.login_b=LoginBusiness(driver)
        self.d1=driver

    def login(self):
        self.login_b.login_base("2071669","111111")
        time.sleep(2)

