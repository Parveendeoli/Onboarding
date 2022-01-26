from selenium.webdriver.common.by import By


class PlanDetail():

    def __init__(self, driver):
        self.driver = driver

        self.annual_report = "Annual Report Filing"
        # self.registered_agent = ""

    def annual(self):
        self.driver.find_elememt(By.LINK_TEXT, self.annual_report).click()
