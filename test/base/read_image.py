# coding=utf-8
import pytesseract
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素
from test.base.find_element import FindElement
from test.handle.login_handle import LoginHandle
from PIL import Image

class ReadImage(object):
    def read_code(self,driver):
        self.save_screenshot(driver)
        self.cut_code(driver)
        image=Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
        text = pytesseract.image_to_string(image)
        print(text)
        return text

    def save_screenshot(self,driver):
        driver.save_screenshot("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")

    def cut_code(self,driver):
        img = FindElement(driver).get_element("code_img")
        frame=FindElement(driver).get_element("frame_html")
        print(frame.location)
        L = img.location["x"]
        T = img.location["y"]
        print(img.location,img.location["x"],img.location["y"])
        R = img.size["width"] + L
        H = img.size["height"] + T
        img = Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
        code=img.crop((L,T,R,H))
        code.save("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")