#coding=utf-8
from test.business.login_business import LoginBusiness
import time
class LoginCase(object):
    def __init__(self,driver):
        self.login_b=LoginBusiness(driver)
        self.d1=driver

    def login(self):
        for i in range(0,4):
            self.login_b.login_base("2076793","111333")
            time.sleep(2)
            self.d1.refresh()

