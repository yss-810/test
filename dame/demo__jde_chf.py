#京东充话费
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.jd.com')
driver.implicitly_wait("10")

print("当前title：",driver.title)
print("当前url",driver.current_url)
print("当前窗口句柄",driver.current_window_handle)
print("所有窗口句柄",driver.window_handles)
#充值业务
driver.find_element_by_link_text('话费').click()


#切换窗口
handles=driver.window_handles
driver.switch_to.window(handles[1])

print("当前title：",driver.title)
print("当前url",driver.current_url)
print("当前窗口句柄",driver.current_window_handle)
print("所有窗口句柄",driver.window_handles)


# driver.find_element_by_class_name('mobile gray').send_keys('15928561321')
#流量充值
driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]/a').click()
time.sleep(2)
#跳入
driver.switch_to.frame('flowiframe')
driver.find_element_by_xpath('//div[@id="phoneitem"]/div/input').send_keys('15928561321')
time.sleep(2)
driver.find_element_by_xpath('//div[@id="flowItem"]/div/ul/li[3]').click()
time.sleep(2)

#跳出
driver.switch_to.parent_frame()
#话费充值
driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[1]').click()
time.sleep(2)
#跳入
driver.switch_to.frame('fast-cziframe')
driver .find_element_by_xpath('//div[@id="phoneitem"]/div/input').send_keys('15928561321')
time.sleep(1)
driver.find_element_by_xpath('//div[@id="rechargeItem"]/div/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@id="submitItem"]/div/input').click()
time.sleep(2)

#跳出
driver.switch_to.parent_frame()
time.sleep(5)
driver.quit()