#coding=utf-8
from test.base.find_element import FindElement

class SendWorkPage(object):
    def __init__(self,driver):
        self.fe=FindElement(driver)

    def get_work_button_element(self):
        self.fe.get_element("work_button")

    def get_my_work_button_element(self):
        self.fe.get_element("my_work_button")
