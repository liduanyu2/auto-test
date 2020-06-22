# coding=utf-8
import time #延时
from selenium import webdriver #webdriver
from selenium.webdriver.support import expected_conditions as EC #检测元素可见
from selenium.webdriver.support.wait import WebDriverWait #持续操作时间
from selenium.webdriver.common.by import By #捕获元素

driver = webdriver.Chrome()
user_name = "2076793"
pass_word = "111111"
#初始化driver

#浏览器初始化
def driver_init():
    driver.get("http://hcloud.bszhihui.com")
    driver.maximize_window()
    time.sleep(1)

#获取element信息
def get_element_classname(class_name):
    element = driver.find_element_by_class_name(class_name)
    return element

def get_element_xpath(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def get_element_id(id):
    element = driver.find_element_by_id(id)
    return element

#检测更改密码(未完工)
def close_changePassWord():
    get_element_id()

def run_main():
    driver_init()
    get_element_classname("imgmb").click()
    time.sleep(1)
    driver.switch_to_frame(get_element_xpath("//*[@id=\"cboxLoadedContent\"]/iframe"))#跳转到frame
    get_element_id("userName").send_keys(user_name)
    get_element_id("passWord").send_keys(pass_word)
    get_element_id("SubmitBt").click()

    locator=(By.CLASS_NAME,"cboxIframe")#获取frame对象
    if WebDriverWait(driver,3).until(EC.presence_of_element_located(locator)):
        driver.switch_to_frame(get_element_xpath("//*[@id=\"cboxLoadedContent\"]/iframe"))#跳转
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/a").click()
        print("找到了")
    else:
        print ("没找到修改密码弹窗")


run_main()
