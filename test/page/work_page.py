#coding=utf-8
from test.base.find_element import FindElement

class WorkPage(object):
    def __init__(self,driver):
        self.fe=FindElement(driver)

    #老师
    #我的备课按钮
    def get_my_work_button(self):
        return self.fe.get_element("my_work_bt")

    #分享按钮
    def get_copy_work_button(self):
        return self.fe.get_element("copy_work_bt")

    #王历选择框
    def get_wangli_checkbox(self):
        return self.fe.get_element("wangli")

    #作业列表frame
    def get_work_frame(self):
        return self.fe.get_element("work_frame")

    #frame
    def get_frame(self):
        return self.fe.get_element("frame")

    #确定分享按钮
    def get_copy_submit_button(self):
        return self.fe.get_element("copy_submit_bt")

    #消息通知按钮
    def get_message_button(self):
        return self.fe.get_element("message_bt")

    #接受分享备课按钮
    def get_get_copy_submit_button(self):
        return self.fe.get_element("get_copy_submit_bt")

    #关闭通知按钮
    def get_close_message_button(self):
        return self.fe.get_element("close_message_bt")

    #发布课前按钮
    def get_release_keqian_button(self):
        return self.fe.get_element("release_keqian_bt")

    #发布课后按钮
    def get_release_kehou_button(self):
        return self.fe.get_element("release_kehou_bt")

    #确认发布按钮
    def get_release_submit_button(self):
        return self.fe.get_element("release_submit_bt")

    #学生