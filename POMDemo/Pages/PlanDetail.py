import time

import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PlanDetail():

    def __init__(self, driver):
        self.driver = driver

        self.annual_report = "//label[@for='formCheck-annual_report_filing']"
        # self.registered_agent = ""

    def annual(self):
        # self.driver.execute_script("window.scrollTo(0, 1000)")
        flag = self.driver.find_element(By.XPATH, self.annual_report)
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        flag.click()
