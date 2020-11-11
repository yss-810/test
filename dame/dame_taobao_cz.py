import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.taobao.com/')
time.sleep(2)
#充值业务
driver.find_element_by_link_text('充话费').click()
time.sleep(2)
print('打印当前url',driver.current_url)

#切换窗口
handles=driver.window_handles
driver.switch_to.window(handles[-1])

print('打印当前url',driver.current_url)
#输入充值号码是及页面

#跳入frame
driver.swicth_to.frame(driver.find_element_by_xpath('/html/body/iframe'))
driver.find_element_by_id('JCZ7').send_keys('15928561321')

time.sleep(2)
driver.find_element_by_xpath('//div[@id="cz"]/form/div[3]/div/ul/li[1]/span').click()


driver.switch_to.parent_frame()
driver.quit()