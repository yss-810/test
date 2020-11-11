import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.jd.com")
driver.implicitly_wait(10)#隐式等待
driver.find_element_by_id('key').send_keys('手机')
driver.implicitly_wait(10)
driver.find_element_by_class_name('button').click()
driver.implicitly_wait(10)
driver.find_element_by_partial_link_text('荣耀Play4T Pro 麒麟810芯片').click()
time.sleep(10)
driver.quit()