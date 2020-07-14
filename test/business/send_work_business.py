#coding=utf-8
from test.handle.send_work_handle import SendWorkHandle
import time
from test.page.work_page import WorkPage

class SendWorkBusiness(object):
    def __init__(self,driver):
        self.swh=SendWorkHandle(driver)
        self.d1=driver

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
        self.swh.quit_frame()
        self.swh.to_frame()
        time.sleep(1)
        if WorkPage(self.d1).get_wangli_checkbox().is_selected() != True:  #判断checkbox是否被勾选
            self.swh.click_wangli_checkbox()
        self.swh.click_get_copy_submit_button()

    #接受备课分享
    def get_copy_work(self):
        self.swh.click_message_button()
        time.sleep(1)
        self.swh.to_frame()
        self.swh.click_get_copy_work_submit_button()
        self.swh.click_close_message_button()

    #发布课前课后作业
    def release_keqian_work(self):
        self.swh.click_my_work_button()
        time.sleep(1)
        #课前
        self.to_work_frame()
        self.swh.click_release_keqian_button()
        time.sleep(1)
        self.swh.quit_frame()
        self.swh.to_frame()
        self.swh.click_release_submit_button()
        time.sleep(1)
        # 课后
        self.swh.quit_frame()
        self.to_work_frame()
        self.swh.click_release_kehou_button()
        time.sleep(1)
        self.swh.quit_frame()
        self.swh.to_frame()
        self.swh.click_release_submit_button()

# if __name__=="__main__":
#     pass