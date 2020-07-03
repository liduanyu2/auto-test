# coding=utf-8
import pytesseract
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素
from test.base.find_element import FindElement
from test.handle.login_handle import LoginHandle
from PIL import ImageEnhance
from PIL import Image
import os

class ReadImage(object):
    def read_code(self,driver):
        self.save_screenshot(driver)
        self.cut_code()
        self.image_set()
        image=Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
        text = pytesseract.image_to_string(image)
        print(text)
        return text

    def save_screenshot(self,driver):
        driver.save_screenshot("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")

    def cut_code(self):
        # img = FindElement(driver).get_element("code_img")
        # L = img.location["x"]
        # T = img.location["y"]
        # R = img.size["width"] + L
        # H = img.size["height"] + T
        img = Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
        code=img.crop((991,456,1093,492))  #((994,456,1098,492))
        code.save("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")

    def image_set(self):
        im = Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")

        # # 提高辨识度
        # im = im.convert('RGB')
        # enhancer = ImageEnhance.Color(im)
        # enhancer = enhancer.enhance(0)
        # enhancer = ImageEnhance.Brightness(enhancer)
        # enhancer = enhancer.enhance(2)
        # enhancer = ImageEnhance.Contrast(enhancer)
        # enhancer = enhancer.enhance(8)
        # enhancer = ImageEnhance.Sharpness(enhancer)
        # im = enhancer.enhance

        # 进行置灰处理
        im = im.convert("L")

        # 这个是二值化阈值
        threshold = 150
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        # 通过表格转换成二进制图片，1的作用是白色，0就是黑色
        im = im.point(table, "1")
        im.save("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
        img = Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
        for i in range(0,20):
            im = self.image_down(img)
            font=("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img"+str(i)+".png")
            im.save(font)

    def image_down(self,im):
        # 传入二值化后的图片进行降噪
        pixdata = im.load()
        w, h = im.size
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                threshold = 252
                count = 0
                if pixdata[x, y - 1] > threshold:  # 上
                    count = count + 1
                if pixdata[x, y + 1] > threshold:  # 下
                    count = count + 1
                if pixdata[x - 1, y] > threshold:  # 左
                    count = count + 1
                if pixdata[x + 1, y] > threshold:  # 右
                    count = count + 1
                if pixdata[x - 1, y - 1] > threshold:  # 左上
                    count = count + 1
                if pixdata[x - 1, y + 1] > threshold:  # 左下
                    count = count + 1
                if pixdata[x + 1, y - 1] > threshold:  # 右上
                    count = count + 1
                if pixdata[x + 1, y + 1] > threshold:  # 右下
                    count = count + 1
                if count > 4:
                    pixdata[x, y] = 255
        return im


    def dalao_de_fangfa(self):
        # path = os.path.dirname(__file__)
        # origin_path = path + '/origin_imgs/'
        # new_path = path + '/clean_imgs/'  # 用来存放处理好的图片
        #
        # # 从100张图片中提取出字符样本
        # for image in os.listdir(origin_path)[:100]:
        #     im = Image.open(origin_path + image)
        #     width, height = im.size
        #
        #     # 获取图片中的颜色，返回列表[(counts, color)...]
        #     color_info = im.getcolors(width * height)
        #     # 按照计数从大到小排列颜色，那么颜色计数最多的应该是背景，接下来排名2到6的则对应5个字符。
        #     sort_color = sorted(color_info, key=lambda x: x[0], reverse=True)
        #
        #     # 根据颜色，提取出每一个字符，重新放置到一个新建的白色背景image对象上。每个image只放一个字符。
        #     char_dict = {}
        #     for i in range(1, 6):
        #         im2 = Image.new('RGB', im.size, (255, 255, 255))
        #         for x in range(im.size[0]):
        #             for y in range(im.size[1]):
        #                 if im.getpixel((x, y)) == sort_color[i][1]:
        #                     im2.putpixel((x, y), (0, 0, 0))
        #                 else:
        #                     im2.putpixel((x, y), (255, 255, 255))
        #         im2.save(new_path + str(i) + '-' + image.replace('jpg', 'tif'))
        #     print('成功处理图片{}'.format(image))
            im = Image.open("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")
            width = im.size["width"]
            height = im.size["height"]
            # 获取图片中的颜色，返回列表[(counts, color)...]
            color_info = im.getcolors(width * height)
            # 按照计数从大到小排列颜色，那么颜色计数最多的应该是背景，接下来排名2到6的则对应5个字符。
            sort_color = sorted(color_info, key=lambda x: x[0], reverse=True)
            # 根据颜色，提取出每一个字符，重新放置到一个新建的白色背景image对象上。每个image只放一个字符。
            char_dict = {}
            for i in range(1, 6):
                im2 = Image.new('RGB', im.size, (255, 255, 255))
                for x in range(im.size[0]):
                    for y in range(im.size[1]):
                        if im.getpixel((x, y)) == sort_color[i][1]:
                            im2.putpixel((x, y), (0, 0, 0))
                        else:
                            im2.putpixel((x, y), (255, 255, 255))
                im2.save("C:/Users/Administrator/Desktop/auto-test/test/screenshot/code_img.png")