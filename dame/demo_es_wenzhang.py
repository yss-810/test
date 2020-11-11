"""
case:后台登录--商品管理--文章管理--文章列表--添加-修改-发布-删除
import：
用户名：admin
密码：LS514320ls
文章标题：逆商


step:
1、登录后台
2、进入左侧导航菜单【文章管理-文章列表】
   2.1点击【文章管理】
   2.2点击【文章列表】
3、进入右侧文章列表页面，添加文章信息
   3.1进入右侧添加页面
   3.2一次输入文章各项信息
   3.3点击【确定】按钮完成添加
4、进入文章列表，查看文章
   4.1进入右侧列表页面
   4.2点击【查看】
   4.3切换回上一个窗口
5、进入文章列表，修改文章
   5.1进入修改页面
   5.2修改文章名
   5.3点击保存
6、进入文章发布
   6.1选择文章
   6.2选择时间
   6.3点击【批量发布】
7、进入文章列表，删除文章
   7.1点击【删除】
   7.2处理弹窗确定
8、退出
"""

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

#访问。打开浏览器登录页面
driver.get('http://localhost/upload/admin')
driver.implicitly_wait(10)#隐式等待
time.sleep(2)
print('当前url',driver.current_url)

# driver.find_element(By.NAME,'remember').click()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('yss123321')
# driver.find_element(By.ID,'remember').click()
driver .find_element(By.CLASS_NAME,'button').click()
driver.implicitly_wait(30)


#进入frame标签
driver.switch_to.frame('menu-frame')

#选择文章列表
driver.find_element_by_xpath('//ul[@id="menu-ul"]/li[6]').click()
time.sleep(1)
driver.find_element_by_link_text('文章列表').click()
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()

#切入frame
driver.switch_to.frame('main-frame')
time.sleep(1)
driver.find_element(By.LINK_TEXT,'添加新文章').click()
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()

#切入frame
driver.switch_to.frame('main-frame')
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input').send_keys('逆商3')
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[2]/td[2]/select').click()
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[2]/td[2]/select/option[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[4]').click()

time.sleep(5)
#退出frame
driver.switch_to.parent_frame()

#切入frame，选择文章列表
driver.switch_to.frame('menu-frame')
driver.find_element_by_xpath('//ul[@id="menu-ul"]/li[6]').click()
time.sleep(1)
driver.find_element_by_link_text('文章列表').click()
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()

#切入frame，查看文章
driver.switch_to.frame('main-frame')
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[2]/td[7]/span/a[1]/img').click()
time.sleep(2)

# 切换窗口
handles=driver.window_handles
driver.switch_to.window(handles[-2])
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()


#修改文章
#切入frame，选择文章列表
driver.switch_to.frame('menu-frame')
driver.find_element_by_xpath('//ul[@id="menu-ul"]/li[6]').click()
time.sleep(1)
driver.find_element_by_link_text('文章列表').click()
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()

#修改文章
driver.switch_to.frame('main-frame')
driver.find_element(By.XPATH,'//table[@id="list-table"]/tbody/tr[7]/td[7]/span/a[2]/img').click()
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input').clear()
time.sleep(1)
driver.find_element(By.XPATH,'//table[@id="general-table"]/tbody/tr[1]/td[2]/input').send_keys('3G普及')
time.sleep(1)
driver.find_element(By.XPATH,'//div[@id="tabbody-div"]/form/div/input[4]').click()
driver.switch_to.parent_frame()#跳出frame标签

#文章发布
driver.switch_to.frame('menu-frame')
driver.find_element_by_xpath('//ul[@id="menu-ul"]/li[6]').click()
time.sleep(1)
driver.find_element_by_link_text('文章自动发布').click()
time.sleep(1)
#退出frame
driver.switch_to.parent_frame()

#切入右侧发布页
driver.switch_to.frame('main-frame')

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[2]/td[1]/input').click()
time.sleep(1)
#日期控件
js="document.getElementById('date').removeAttribute('readonly')"
driver.execute_script(js)
time.sleep(2)
driver.find_element(By.ID,"date").send_keys('2020-08-18')

driver.find_element(By.ID,('btnSubmit1')).click()

driver.switch_to.parent_frame()#跳出frame标签
#删除文章
driver.switch_to.frame('menu-frame')
driver.find_element(By.LINK_TEXT,('文章列表')).click()
driver.switch_to.parent_frame()
#切入右侧发布页
driver.switch_to.frame('main-frame')
time.sleep(2)
driver.find_element(By.XPATH,('//table[@id="list-table"]/tbody/tr[7]/td[7]/span/a[3]/img')).click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.switch_to.parent_frame()
#删除文章












time.sleep(3)
driver.quit()