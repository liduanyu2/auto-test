#coding=utf-8
from test.base.find_element import FindElement

class SendWorkPage(object):
    def __init__(self,driver):
        self.fe=FindElement(driver)

    #备课按钮
    def get_work_button_element(self):
        return self.fe.get_element("work_bt")

    #我的备课按钮
    def get_my_work_button_element(self):
        return self.fe.get_element("my_work_bt")

    #分享按钮
    def get_copy_work_button_element(self):
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
    def get_copy_submit_button_element(self):
        return self.fe.get_element("copy_submit_bt")

    #消息通知按钮
    def get