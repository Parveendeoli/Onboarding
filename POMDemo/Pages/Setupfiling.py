from selenium.webdriver.common.by import By


class Setup():

    def __init__(self, driver):
        self.driver = driver

        self.i_got_this_xpath = "//label[@class='form-check-label d-flex flex-column justify-content-center align-items-center gotThis-checked']"
        self.next_button_xpath = "//button[@class='btn btn-primary next']"

    def i_got(self):
        self.driver.find_element(By.XPATH, self.i_got_this_xpath).click()

    def next(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()
