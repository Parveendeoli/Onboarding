class Setup():

    def __init__(self, driver):
        self.driver = driver

        self.i_got_this_xpath = "//label[@class='form-check-label d-flex flex-column justify-content-center align-items-center gotThis-checked']"
        self.next_button_xpath = "//button[@class='btn btn-primary next']"

    def i_got(self):
        self.driver.find_element_by_xpath(self.i_got_this_xpath).click()

    def next(self):
        self.driver.find_element_by_xpath(self.next_button_xpath).click()


