#coding=utf-8
from selenium import webdriver
from test.base.find_element import FindElement
class SetFrame(object):
    def __init__(self,driver):
        self.sf=driver

    def to_frame(self,key):
        self.sf.switch_to.frame(FindElement(self.sf).get_element(key))

    def quit_frame(self):
        self.sf.switch_to.default_content()