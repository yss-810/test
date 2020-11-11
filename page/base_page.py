class BasePage():
    def open(self):
        self.driver.get(self.url)