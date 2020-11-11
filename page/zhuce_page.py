from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ZhucePage(BasePage):
    def __init__(self,driver):
        self.driver=driver
        # 定位器
        self.locator_ele_username = (By.NAME, ("username"))  # 用户名
        self.locator_ele_email = (By.NAME, ("email"))  # 邮箱
        self.locator_ele_password = (By.NAME, ("password"))  # 密码
        self.locator_ele_confirm_password = (By.NAME, ("confirm_password"))  # 确认密码
        self.locator_ele_qq = (By.NAME, ("extend_field2"))  # qq号
        self.locator_ele_mobile = (By.NAME, ("extend_field5"))  # 手机号
        self.locator_ele_Submit = (By.NAME, ("Submit"))  # 提交注册
        self.locator_ele_assert = (By.XPATH, ('//font[@id="ECS_MEMBERZONE"]/a[1]'))  # 断言
        self.url='http://localhost/upload/user.php?act=register'

    def ele_username(self,username):
        self.driver.find_element(*self.locator_ele_username).send_keys(username)

    def ele_email(self,email):
        self.driver.find_element(*self.locator_ele_email).send_keys(email)

    def ele_password(self,password):
        self.driver.find_element(*self.locator_ele_password).send_keys(password)

    def ele_confirm_password(self,confirm_password):
        self.driver.find_element(*self.locator_ele_confirm_password).send_keys(confirm_password)

    def ele_qq(self,qq):
        self.driver.find_element(*self.locator_ele_qq).send_keys(qq)

    def ele_mobile(self,mobile):
        self.driver.find_element(*self.locator_ele_mobile).send_keys(mobile)
    def ele_Submit(self):
        self.driver.find_element(*self.locator_ele_Submit).click()

    def ele_assert(self):
        result=self.driver.find_element(*self.locator_ele_assert).text
        return result


    def zhuce(self,username,email,password,confirm_password,qq,mobile):
        self.open()
        self.ele_username(username)
        self.ele_email(email)
        self.ele_password(password)
        self.ele_confirm_password(confirm_password)
        self.ele_qq(qq)
        self.ele_mobile(mobile)
        self.ele_Submit()
        assert_result=self.ele_assert()
        return assert_result


