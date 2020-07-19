#coding=utf-8
from test.base.find_element import FindElement
class IndexPage(object):
    def __init__(self,driver):
        self.fe=FindElement(driver)
    
    #老师
    #备课按钮
    def get_work_button(self):
        return self.fe.get_element("work_bt")