# coding=utf-8
import pytesseract
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素
from test.base.find_element import FindElement
from PIL import Image
class ReadImage(object):
    def read_code(self,driver):
        image = Image.open("#文件路径")
        text = pytesseract.image_to_string(image)
        return text