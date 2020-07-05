#coding=utf-8
from test.handle.send_work_handle import SendWorkHandle
import time

class SendWorkBusiness(object):
    def __init__(self,driver):
        self.swh=SendWorkHandle(driver)

    #去备课页面
    def go_work(self):
        self.swh.click_work_button()

    #去我的备课列表
    def go_my_work(self):
        self.go_work()
        time.sleep(1)
        self.swh.click_my_work_button()

    #分享备课
    def copy_work(self):
        self.swh.click_copy_work_button()

    #跳转到备课列表frame
    def to_work_frame(self):
        self.swh.to_work_frame()

    #跳转到frame中
    def to_frame(self):
        self.swh.to_frame()

    #分享备课给王历
    def copy_work_to_wangli(self):
        self.swh.to_work_frame()
        self.swh.click_copy_work_button()
        time.sleep(1)
        self.swh.to_frame()
        time.sleep(1)
        self.swh.click_wangli_button()
        self.swh.click_get_copy_submit_button()