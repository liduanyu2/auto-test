#coding=utf-8
from test.page.send_work_page import SendWorkPage
from test.base.set_frame import SetFrame

class SendWorkHandle(object):
    def __init__(self,driver):
        self.swp=SendWorkPage(driver)
        self.frame=SetFrame(driver)

    #点击备课
    def click_work_button(self):
        self.swp.get_work_button_element().click()

    #点击我的备课
    def click_my_work_button(self):
        self.swp.get_my_work_button_element().click()

    #点击分享按钮
    def click_copy_work_button(self):
        self.swp.get_copy_work_button_element().click()

    #跳转到被俄刻frame
    def to_work_frame(self):
        self.frame.to_frame("work_frame")

    #跳转到frame
    def to_copy_frame(self):
        self.frame.to_frame("copy_frame")

    def quit_frame(self):
        self.frame.quit_frame()

    #点击王历选择框
    def click_wangli_button(self):
        print(self.swp.get_wangli_element())
        self.swp.get_wangli_element().click()

    #点击确定分享
    def click_get_copy_submit_button(self):
        self.swp.get_copy_submit_button_element().click()