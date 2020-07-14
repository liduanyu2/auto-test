#coding=utf-8
import unittest
from selenium import webdriver
from test.business.login_business import LoginBusiness
from test.business.send_work_business import SendWorkBusiness

from test.page.work_page import WorkPage
import os
import time

class ReTestTea(unittest.TestCase):

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
        LoginBusiness(self.driver).login_base("2129448","111111")
        print("\n登录结束")

    #分享备课
    def test_send_work(self):
        SendWorkBusiness(self.driver).go_my_work()
        time.sleep(1)
        SendWorkBusiness(self.driver).copy_work_to_wangli()
        # self.driver.find_element_by_xpath("//*[@id=\"addBtn\"]").click()
        print("\n分享备课结束")

    #接受分享备课
    def test_get_work(self):
        SendWorkBusiness(self.driver).get_copy_work()
        print("\n接受分享备课结束")

    #发布课前预习作业
    def test_send_keqiankehou(self):
        SendWorkBusiness(self.driver).release_keqian_work()
        print("\n发布课前预习结束")

if __name__=="__main__":
    suite = unittest.TestSuite()
    runner=unittest.TextTestRunner()
    suite.addTest(ReTestTea("test_login"))
    suite.addTest(ReTestTea("test_send_work"))
    suite.addTest(ReTestTea("test_get_work"))
    suite.addTest(ReTestTea("test_send_keqiankehou"))
    runner.run(suite)