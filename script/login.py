import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

#打开浏览器
driver.get('http://192.168.4.223/upload/')
#业务登录
driver.find_element(By.XPATH,('//*[@id="ECS_MEMBERZONE"]/a[1]')).click()
driver.find_element(By.XPATH,('/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input')).send_keys('admin3')
driver.find_element(By.XPATH,('/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[2]/td[2]/input')).send_keys('LS514320ls')
driver.find_element(By.XPATH,('/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]')).click()



time.sleep(3)
driver.quit()