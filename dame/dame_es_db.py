"""
case:后台登录--数据库管理--数据备份--数据表优化--SQL查询-转换数据
import：
用户名：admin
密码：yss123321

step:
1、登录后台
2、进入左侧导航菜单【数据库管理-数据备份】
   2.1点击【数据库管理】
   2.2点击【数据备份】
3、进入左侧导航菜单【数据库管理-数据表优化】
   3.1点击【数据库管理】
   3.2点击【数据表优化】
4、进入左侧导航菜单【数据库管理-SQL查询】
   4.1点击【数据库管理】
   4.2点击【SQL查询】
5、进入左侧导航菜单【数据库管理-转换数据】
   5.1点击【数据库管理】
   5.2点击【转换数据】
6、退出
"""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

#访问。打开浏览器登录页面
driver.get('http://192.168.4.231/upload/admin')
driver.implicitly_wait(10)#隐式等待
time.sleep(2)
print('当前url',driver.current_url)

# driver.find_element(By.NAME,'remember').click()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('yss123321')
# driver.find_element(By.ID,'remember').click()
driver .find_element(By.CLASS_NAME,'button').click()
driver.implicitly_wait(30)

#数据备份
driver.switch_to.frame('menu-frame')
time.sleep(4)
driver.find_element(By.XPATH,('//ul[@id="menu-ul"]/li[11]/ul/li[1]/a')).click()
time.sleep(1)
driver.switch_to.parent_frame()

driver.switch_to.frame('main-frame')
time.sleep(4)
driver.find_element(By.XPATH,('//div[@id="listDiv"]/center/input')).click()
time.sleep(1)
driver.switch_to.parent_frame()







time.sleep(3)
driver.quit()