
from selenium.webdriver.common.by import By

"""页面封装"""
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.locator_ele_username=(By.XPATH,('/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[1]/td[2]/input'))
        self.locator_ele_password=(By.XPATH,('/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[2]/td[2]/input'))
        self.locator_ele_submit=(By.XPATH,('/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]'))
        self.locator_ele_rasser=(By.XPATH, ('//font[@id="ECS_MEMBERZONE"]/a[1]'))
        self.url="http://192.168.4.231/upload/user.php"

    def ele_username(self,username):
        self.driver.find_element(*self.locator_ele_username).send_keys(username)
    def ele_password(self,password):
        self.driver.find_element(*self.locator_ele_password).send_keys(password)
    def ele_submit(self):
        self.driver.find_element(*self.locator_ele_submit).click()

    def ele_rasser(self):
        result = self.driver.find_element(*self.locator_ele_rasser).text
        return result
    def open(self):
        self.driver.get(self.url)

    def login(self,username,password):
        self.open()
        self.ele_username(username)
        self.ele_password(password)
        self.ele_submit()
        assert_reuslt=self.ele_rasser()
        return assert_reuslt