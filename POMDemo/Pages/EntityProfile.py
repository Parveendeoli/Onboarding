from selenium.webdriver.support.select import Select


class Entity():

    def __init__(self, driver):
        self.select = None
        self.driver = driver

        self.Entity_Name_xpath = "//input[@placeholder='Entity Name*']"
        self.State_name = "state[]"
        self.Formation_xpath = "//input[@placeholder='Formation Date']"
        self.Entity_Number_xpath = "//input[@placeholder='Entity Number']"
        self.Entity_Type_name = "type[]"
        self.Next_Button_xpath = "//button[@class='btn btn-primary next']"

    def entity_name(self, entityname):
        self.driver.find_element_by_xpath(self.Entity_Name_xpath).clear()
        self.driver.find_element_by_xpath(self.Entity_Name_xpath).send_keys(entityname)

    def state(self):
        self.select = Select(self.driver.find_element_by_name(self.State_name))
        self.select.select_by_visible_text("California")

    def formation(self, formation):
        self.driver.find_element_by_xpath(self.Formation_xpath).clear()
        self.driver.find_element_by_xpath(self.Formation_xpath).send_keys(formation)

    def entity_number(self, entitynumber):
        self.driver.find_element_by_xpath(self.Entity_Name_xpath).clear()
        self.driver.find_element_by_xpath(self.Entity_Name_xpath).send_keys(entitynumber)

    def entity_type(self):
        self.select = Select(self.driver.find_element_by_name(self.Entity_Type_name))
        self.select.select_by_visible_text("LLC")

    def next(self):
        self.driver.find_element_by_xpath(self.Next_Button_xpath).click()
