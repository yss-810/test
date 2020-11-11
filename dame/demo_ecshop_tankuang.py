"""
case:ecshop收藏本站
step:
1、打开网页
2、登录
3、收藏网页
4、退出
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#打开浏览器登录页面
driver.get('http://192.168.4.223/upload/')
driver.implicitly_wait(10)#隐式等待
time.sleep(2)
#登录
driver.find_element_by_link_text('登录').click()
time.sleep(2)
#输入
driver.find_element_by_name("username").send_keys('admin3')
driver.find_element_by_name("password").send_keys('LS514320ls')
driver.find_element_by_name("remember").click()
driver.find_element_by_name("submit").click()
time.sleep(1)

#收藏本站，弹框处理
driver.find_element(By.LINK_TEXT,'收藏本站').click()



time.sleep(3)
# driver.switch_to.alert.text
driver.switch_to.alert.accept()



time.sleep(3)
driver.quit()