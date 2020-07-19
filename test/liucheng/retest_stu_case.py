#coding=utf-8
import unittest
from selenium import webdriver
from test.business.login_business import LoginBusiness
from test.business.send_work_business import SendWorkBusiness

from test.page.work_page import WorkPage
import os
import time

class ReTestStu(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()  # .create_options("--user-data-dir="+os.getenv("USERPROFILE")+"/AppData/Local/Google/Chrome/User Data/Default")
        self.driver.maximize_window()
        self.driver.get("http://uat-hcloud.bszhihui.com")
        time.sleep(1)

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    #登录
    def test_login(self):
        LoginBusiness(self.driver).login_base("2129484","111111")
        print("\n登录结束")

    #分享备课
    def test_send_work(self):
        SendWorkBusiness(self.driver).go_my_work()

if __name__=="__main__":
    suite = unittest.TestSuite()
    runner=unittest.TextTestRunner()
    suite.addTest(ReTestStu("test_login"))
    suite.addTest(ReTestStu("test_send_work"))

    runner.run(suite)