#coding=utf-8
from selenium import webdriver
import os
import time
from test.base.find_element import FindElement

class FileUpload(object):
    def __init__(self,driver):
        ub=FindElement(driver).get_element("upload_bt")

