#coding=utf-8
# coding=utf-8
import time #延时
from selenium import webdriver #webdriver
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素
from test.case.login_case import LoginCase
from test.base.set_frame import SetFrame
from test.case.login_case import LoginCase
from test.page.login_page import LoginPage
from test.handle.login_handle import LoginHandle
from test.base.find_element import FindElement
import unittest

#driver初始化
# driver = webdriver.Chrome()
# driver.get("http://hcloud.bszhihui.com")
# driver.maximize_window()

#老师登录
LoginCase().unittest.main()
