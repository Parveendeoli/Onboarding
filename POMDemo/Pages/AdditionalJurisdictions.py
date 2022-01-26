import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Jurisdiction():

    def __init__(self, driver):
        self.select = None
        self.driver = driver

        self.Add_Jurisdiction_button_xpath = "//span[@class='collapse-title-long']"
        self.Add_Another_button_xpath = "//button[@class='btn float-right btn-plain btn-addmore p-0']"
        self.Entity_Name_name = "jurisdiction[1][name][]"
        self.Select_State_name = "jurisdiction[1][state][]"
        self.Formation_Date_xpath = "//input[@class='form-control datepicker entity-date registration-date-fetch-field']"
        self.Jurisdiction_Number_xpath = "//input[@placeholder='Jurisdiction Number']"
        self.Entity_Type_xpath = "//select[@name='jurisdiction[1][type][]']"
        self.Next = "//button[@class='btn btn-primary next']"
        self.chat_xpath = "//div[@class='VizExIcon__IconWrapper-u2jepa-0 gzEoLT']"

    def jurisdiction(self):
        self.driver.find_element(By.XPATH, self.Add_Jurisdiction_button_xpath).click()

    def add(self):
        self.driver.find_element(By.XPATH, self.Add_Another_button_xpath).click()

    def entity_name(self, name):
        self.driver.find_element(By.NAME, self.Entity_Name_name).clear()
        self.driver.find_element(By.NAME, self.Entity_Name_name).send_keys(name)

    def state(self):
        self.select = Select(self.driver.find_element(By.NAME, self.Select_State_name))
        self.select.select_by_visible_text("Delaware")

    def formation_date(self, date):
        self.driver.find_element(By.XPATH, self.Formation_Date_xpath).clear()
        self.driver.find_element(By.XPATH, self.Formation_Date_xpath).send_keys(date)

    def jurisdiction_number(self, number):
        self.driver.find_element(By.XPATH, self.Jurisdiction_Number_xpath).clear()
        self.driver.find_element(By.XPATH, self.Jurisdiction_Number_xpath).send_keys(number)

    def entity_type(self):
        self.select = Select(self.driver.find_element(By.XPATH, self.Entity_Type_xpath))
        self.select.select_by_visible_text("LLC")

    def chat_button(self):
        time.sleep(25)
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH, self.chat_xpath).click()
        self.driver.switch_to.default_content()

    def next(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element(By.XPATH, self.Next).click()
