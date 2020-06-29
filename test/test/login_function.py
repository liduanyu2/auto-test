#coding=utf-8
import time #延时
from selenium import webdriver #webdriver
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素
from test.test.find_element import FindElement
class login_function(object):
    def __init__(self,url):
        self.driver=self.get_driver(url)
       # time.sleep(3)

    #webdriver初始化
    def get_driver(self,url):
        driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息
    def send_user_info(self,key,data):
        element=self.get_element(key)
        element.send_keys(data)

    #定位element
    def get_element(self,key):
        element=FindElement(self.driver).get_element(key)
        return element

    def switch_to_frame(self,key):
        self.driver.switch_to_frame(self.get_element(key))

    def main(self):
        self.get_element("login_bt").click()
        time.sleep(1)
        self.switch_to_frame("frame")
        self.send_user_info("username","2071669")
        self.send_user_info("password","111111")
        self.get_element("login_summit_bt").click()

        locator = (By.CLASS_NAME, "cboxIframe")  # 获取frame对象
        print(locator)
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator)):
            self.switch_to_frame("frame") # 跳转
            self.get_element("frame_close").click()
            print("找到了")
        else:
            print("没找到修改密码弹窗")

if __name__=="__main__":
    login_function("http://hcloud.bszhihui.com").main()