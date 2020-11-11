#百度搜索关键字

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
#访问
driver.get("http://www.baidu.com")
driver.implicitly_wait(20)
#操作
driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_partial_link_text('Python(计算机程序设计语言)_百度百科').click()
time.sleep(10)
# driver.back()
# driver.find_element_by_name('wd').send_keys("linux")
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.find_element_by_name('wd').clear()
# time.sleep(3)
# driver.find_element_by_class_name('s_ipt').send_keys("自动化")
# driver.find_element_by_id('su').click()



# time.sleep(2)
#关闭
driver.quit()