"""
case:后台登录--报表统计--流量分析--客户统计--订单统计-销售明细-销售排行
import：
用户名：admin
密码：yss123321

step:
1、登录后台
2、进入左侧导航菜单【报表统计-流量分析】
   2.1点击【报表统计】
   2.2点击【流量分析】
3、进入左侧导航菜单【报表统计-客户统计】
   3.1进入右侧添加页面
   3.2点击【客户统计报表下载】
4、进入左侧导航菜单【报表统计-订单统计】
   4.1进入右侧列表页面
   4.2搜索订单
   4.3切换回上一个窗口
5、进入左侧导航菜单【报表统计-销售明细】
   5.1进入右侧页面
   5.2搜索销售明细
   5.3切换回上一个窗口
6、进入左侧导航菜单【报表统计-销售排行】
   6.1进入右侧页面
   6.2搜索销售明细
   6.3切换回上一个窗口

7、退出
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

#客户统计
driver.switch_to.frame('menu-frame')
time.sleep(1)
driver.find_element(By.XPATH,('//ul[@id="menu-ul"]/li[5]')).click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,('流量分析')).click()
time.sleep(2)
driver.switch_to.parent_frame()
#流量分析-查询
driver.switch_to.frame('main-frame')
time.sleep(2)
driver.find_element(By.XPATH,('//form[@id="selectForm"]/input[1]')).clear()
time.sleep(1)
driver.find_element(By.XPATH,('//form[@id="selectForm"]/input[1]')).send_keys('2020-01-01')
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[2]')).clear()
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[2]')).send_keys('2020-08-17')
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[3]')).click()
time.sleep(1)
driver.switch_to.parent_frame()
#客户统计
driver.switch_to.frame('menu-frame')
time.sleep(3)
driver.find_element(By.XPATH,('//ul[@id="menu-ul"]/li[5]/ul/li[2]/a')).click()
time.sleep(1)
driver.switch_to.parent_frame()
#订单统计
driver.switch_to.frame('menu-frame')
time.sleep(2)
driver.find_element(By.LINK_TEXT,('订单统计')).click()
time.sleep(2)
driver.switch_to.parent_frame()

driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[1]')).clear()
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[1]')).send_keys('2020-01-01')
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[2]')).clear()
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[2]')).send_keys('2020-08-17')
time.sleep(1)
driver.find_element(By.XPATH,('//Form[@id="selectForm"]/input[3]')).click()
driver.switch_to.parent_frame()

#销售明细
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,('//ul[@id="menu-ul"]/li[5]/ul/li[6]/a')).click()
driver.switch_to.parent_frame()

#销售排行
driver.switch_to.frame('menu-frame')
driver.find_element(By.XPATH,('//ul[@id="menu-ul"]/li[5]/ul/li[8]/a')).click()
driver.switch_to.parent_frame()

















time.sleep(3)
driver.quit()