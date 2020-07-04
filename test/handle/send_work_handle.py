#coding=utf-8
from test.page.send_work_page import SendWorkPage

class SendWorkHandle(object):
    def __init__(self,driver):
        self.swp=SendWorkPage(driver)

    def click_work_button(self):
        self.swp.get_work_button_element().click()

    def click_my_work_button(self):
        self.swp.get_my_work_button_element().click()