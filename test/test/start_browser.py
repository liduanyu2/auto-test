# coding=utf-8
import time
from selenium import webdriver

driver1 = webdriver.Chrome()
driver1.get("http://hcloud.bszhihui.com")
time.sleep(1)
driver1.find_element_by_class_name("imgmb").click()
time.sleep(1)
frame = driver1.find_element_by_xpath("//*[@id=\"cboxLoadedContent\"]/iframe")
driver1.switch_to_frame(frame)
driver1.find_element_by_id("userName").send_keys("2076793")
driver1.find_element_by_id("passWord").send_keys("111111")
driver1.find_element_by_id("SubmitBt").click()
