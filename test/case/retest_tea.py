#coding=utf-8
import unittest
from selenium import webdriver
from test.business.login_business import LoginBusiness
from test.business.send_work_business import SendWorkBusiness
import os

class ReTestTea(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome()  # .create_options("--user-data-dir="+os.getenv("USERPROFILE")+"/AppData/Local/Google/Chrome/User Data/Default")
        driver.maximize_window()



    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        LoginBusiness(self.driver).login_base("2071669","111111")

    def test_send_work(self):
        SendWorkBusiness(self.driver).go_my_work()

if __name__=="__main__":
    unittest.main()