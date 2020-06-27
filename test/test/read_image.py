# coding=utf-8
import pytesseract
from PIL import Image

image = Image.open("#文件路径")
text = pytesseract.image_to_string(image)
print(text)

# coding=utf-8
import time #延时
from selenium import webdriver #webdriver
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素
class UserLogin(object):
    def __int__(self,url):
        self.driver=self.get_driver(url)
    #获取driver并且打开url
    def get_driver(self,url):
        driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)
        return
    #输入用户信息
    def send_user_info(self):

    def get_user_element(self):
