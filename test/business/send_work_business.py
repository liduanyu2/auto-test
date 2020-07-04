#coding=utf-8
from test.handle.send_work_handle import SendWorkHandle
class SendWorkBusiness(object):
    def __init__(self,driver):
        self.swb=SendWorkHandle(driver)

    def go_work(self):
        self.swb.click_work_button()

    def go_my_work(self):
        self.go_work()
        self.swb.click_my_work_button()

