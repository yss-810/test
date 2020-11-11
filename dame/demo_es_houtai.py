"""
case:后台添加商品
import：
用户名：admin
密码：LS514320ls
商品名称：牛仔外套
本店售价：100
促销日期：2020-08-20
修改页商品名称：羊毛大衣

step:
1、登录后台
2、进入左侧导航菜单【商品管理-添加新商品】
   2.1点击【商品管理】
   2.2点击【添加新商品】
3、进入右侧商品添加页面，添加商品信息
   3.1进入右侧添加页面
   3.2一次输入商品各项信息
   3.3点击【确定】按钮完成添加
4、进入商品列表，查看商品
   4.1进入右侧列表页面
   4.2点击【查看】
   4.3切换回上一个窗口
5、进入商品列表，修改商品
   5.1进入修改页面
   5.2修改商品名
   5.3点击保存
6、进入商品列表，删除商品
   6.1点击【删除】
   6.2处理弹窗确定
7、退出
"""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

#访问。打开浏览器登录页面
driver.get('http://192.168.4.223/upload/admin')
driver.implicitly_wait(10)#隐式等待
time.sleep(2)
print('当前url',driver.current_url)
#进行登录
# driver.find_element_by_name("remember").click()
# driver.implicitly_wait(10)#隐式等待
# driver.find_element_by_name("username").send_keys('admin')
# driver.find_element_by_name("password").send_keys('LS514320ls')
# driver.find_element_by_id("remember").click()
# # driver.find_element_by_name("remember").click()
# driver.find_element_by_class_name("button").click()
# driver.implicitly_wait(10)#隐式等待

# driver.find_element(By.NAME,'remember').click()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('LS514320ls')
# driver.find_element(By.ID,'remember').click()
driver .find_element(By.CLASS_NAME,'button').click()
driver.implicitly_wait(30)

#切换窗口
# handles=driver.window_handles
# driver.switch_to.window(handles[-1])
# time.sleep(2)
# print('当前url',driver.current_url)
#进入frame标签
driver.switch_to.frame('menu-frame')

#选择添加商品
driver.find_element_by_xpath('//ul[@id="menu-ul"]/li[1]').click()
time.sleep(2)
driver.find_element_by_link_text('添加新商品').click()
time.sleep(2)

#退出frame
driver.switch_to.parent_frame()

#跳入输入frame
driver.switch_to.frame('main-frame')
driver.find_element_by_xpath('//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys('牛仔外套')

driver.find_element_by_xpath('//table[@id="general-table"]/tbody/tr[3]/td[2]/select').click()

time.sleep(2)
# select=Select(locator)
# select.select_by_visible_text('女装')
#显示等待
wait=WebDriverWait(driver,10,0.5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//select[@name="cat_id"]/option[3]')))

driver.find_element_by_xpath('//select[@name="cat_id"]/option[3]').click()

driver.find_element_by_name('shop_price').send_keys('100')
time.sleep(2)

driver.find_element(By.XPATH,'//input[@id="is_promote"]').click()#点击促销价

time.sleep(2)
#去除前端readonly属性
js = "document.getElementById('promote_start_date').removeAttribute('readonly')"
driver.execute_script(js)
time.sleep(2)
driver.find_element(By.ID,'promote_start_date').clear()
driver.find_element(By.ID,'promote_start_date').send_keys('2020-08-20')

# #图片上传
# # driver.find_element(By.XPATH,'//tablet[@id="general-table"]/tbody/tr[15]/td[2]/input[1]').click()
# driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[15]/td[2]/input[2]').clear()
# time.sleep(2)
# driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[15]/td[2]/input[2]').send_keys(r'F:\1.jpg')


time.sleep(2)

driver.find_element_by_xpath('//div[@id="tabbody-div"]/form/div/input[2]').click()
time.sleep(3)
#查看商品
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[1]/img').click()
time.sleep(2)
#切换窗口到商品管理页面
handles=driver.window_handles
driver.switch_to.window(handles[-2])
time.sleep(2)

#修改商品
driver.switch_to.frame('main-frame')#切入frame标签
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[2]/img').click()
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').clear()
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys('羊毛大衣')
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[2]').click()
driver.switch_to.parent_frame()#跳出frame标签

#删除商品
driver.switch_to.frame('main-frame')
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[4]/img').click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[11]/a[4]/img').click()
time.sleep(2)
driver.switch_to.alert.accept()

driver.switch_to.parent_frame()#跳出frame标签


# driver.implicitly_wait(20)
time.sleep(20)
driver.switch_to.parent_frame()
driver.quit()