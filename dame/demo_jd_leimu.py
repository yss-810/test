import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.jd.com')

#鼠标悬停
# driver.find_element(By.XPATH,'//div[@id="J_cate"]/ul/li[9]/a[1]')
locator=driver.find_element(By.LINK_TEXT,'房产')
action = ActionChains(driver)
action.move_to_element(locator).perform()
time.sleep(5)
driver.find_element(By.LINK_TEXT,'别墅').click()

time.sleep(3)
#切换窗口
handles=driver.window_handles
driver.switch_to.window(handles[-1])

#搜索业务--鼠标
driver.find_element(By.XPATH,'//input[@id="key"]').send_keys('天宸原著')
driver.find_element(By.XPATH,'//input[@id="key"]').send_keys(Keys.ENTER)

time.sleep(5)

#删除业务--鼠标
driver.find_element(By.XPATH,'//input[@id="key"]').send_keys(Keys.CONTROL,"a")
driver.find_element(By.XPATH,'//input[@id="key"]').send_keys(Keys.BACK_SPACE)

# #重复删除
# for i in 5:
#     driver.find_element(By.XPATH, '//input[@id="key"]').send_keys(Keys.BACK_SPACE)
    







time.sleep(5)
driver.quit()