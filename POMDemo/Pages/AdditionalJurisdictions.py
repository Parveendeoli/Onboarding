from selenium.webdriver.support.select import Select


class Jurisdiction():

    def __init__(self, driver):
        self.select = None
        self.driver = driver

        self.Add_Jurisdiction_button_xpath = "//button[@class='btn btn-primary next']"
        self.Add_Another_button_xpath = "//button[@class='btn float-right btn-plain btn-addmore p-0']"
        self.Entity_Name_name = "jurisdiction[1][name][]"
        self.Select_State_name = "jurisdiction[1][state][]"
        self.Formation_Date_xpath = "//input[@class='form-control datepicker entity-date registration-date-fetch-field']"
        self.Jurisdiction_Number_xpath = "//input[@placeholder='Jurisdiction Number']"
        self.Entity_Type_xpath = "//select[@name='jurisdiction[1][type][]']"
        self.Next = "//button[@class='btn btn-primary next']"

    def jurisdiction(self):
        self.driver.find_element_by_xpath(self.Add_Jurisdiction_button_xpath).click()

    def add(self):
        self.driver.find_element_by_xpath(self.Add_Another_button_xpath).click()

    def entityname(self, name):
        self.driver.find_element_by_name(self.Entity_Name_name).clear()
        self.driver.find_element_by_name(self.Entity_Name_name).send_keys(name)

    def state(self):
        self.select = Select(self.driver.find_element_by_name(self.Select_State_name))
        self.select.select_by_visible_text("California")

    def formation_date(self, date):
        self.driver.find_element_by_xpath(self.Formation_Date_xpath).send_keys(date)

    def jurisdiction_number(self, number):
        self.driver.find_element_by_xpath(self.Jurisdiction_Number_xpath).clear()
        self.driver.find_element_by_xpath(self.Jurisdiction_Number_xpath).send_keys(number)

    def entity_type(self):
        self.select = Select(self.driver.find_element_by_xpath(self.Entity_Type_xpath))
        self.select.select_by_visible_text("LLC")

    def next(self):
        self.driver.find_element_by_xpath(self.Next).click()