from  selenium import webdriver
"""封装浏览器驱动"""
def chrome_browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    return driver

def firefox_browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)

    return driver

# chrome_browser()