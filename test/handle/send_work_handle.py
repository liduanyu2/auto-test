#coding=utf-8
from test.page.work_page import WorkPage
from test.base.set_frame import SetFrame

class SendWorkHandle(object):
    def __init__(self,driver):
        self.wp=WorkPage(driver)
        self.frame=SetFrame(driver)

    #点击备课
    def click_work_button(self):
        self.wp.get_work_button().click()

    #点击我的备课
    def click_my_work_button(self):
        self.wp.get_my_work_button().click()

    #点击分享按钮
    def click_copy_work_button(self):
        self.wp.get_copy_work_button().click()

    #跳转到被俄刻frame
    def to_work_frame(self):
        self.frame.to_frame("work_frame")

    #跳转到frame
    def to_frame(self):
        self.frame.to_frame("copy_frame")

    def quit_frame(self):
        self.frame.quit_frame()

    #点击王历选择框
    def click_wangli_checkbox(self):
        self.wp.get_wangli_checkbox().click()

    #点击确定分享
    def click_get_copy_submit_button(self):
        self.wp.get_copy_submit_button().click()

    #点击消息通知按钮
    def click_message_button(self):
        self.wp.get_message_button().click()

    #点击接受分享备课按钮
    def click_get_copy_work_submit_button(self):
        self.wp.get_get_copy_submit_button().click()

    #点击关闭通知按钮
    def click_close_message_button(self):
        self.wp.get_close_message_button().click()

    #点击发布课前按钮
    def click_release_keqian_button(self):
        self.wp.get_release_keqian_button().click()

    #点击发布课后按钮
    def click_release_kehou_button(self):
        self.wp.get_release_kehou_button().click()

    #点击确认发布按钮
    def click_release_submit_button(self):
        self.wp.get_release_submit_button().click()