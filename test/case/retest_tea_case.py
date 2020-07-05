#coding=utf-8
import unittest
from selenium import webdriver
from test.business.login_business import LoginBusiness
from test.business.send_work_business import SendWorkBusiness
import os
import time

class ReTestTea(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()  # .create_options("--user-data-dir="+os.getenv("USERPROFILE")+"/AppData/Local/Google/Chrome/User Data/Default")
        self.driver.maximize_window()
        self.driver.get("http://hcloud.bszhihui.com")
        time.sleep(1)

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    def test_login(self):
        LoginBusiness(self.driver).login_base("2071669","111111")

    def test_send_work(self):
        SendWorkBusiness(self.driver).go_my_work()
        SendWorkBusiness(self.driver).copy_work_to_wangli()

if __name__=="__main__":
    unittest.main()