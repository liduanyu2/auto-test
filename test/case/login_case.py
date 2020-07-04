#coding=utf-8
from test.business.login_business import LoginBusiness
from selenium import webdriver
import time
import unittest

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://hcloud.bszhihui.com")
        self.driver.maximize_window()
        self.login_b=LoginBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_Login(self):
        self.login_b.login_base("2071669","111111")

    def test_login_err_username(self):
        self.login_b.login_base(None,"111111")

    def test_login_err_password(self):
        self.login_b.login_base("2071669","1111111")

if __name__ == '__main__':
    unittest.main()
