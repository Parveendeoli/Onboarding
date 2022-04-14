from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


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
        self.chat_xpath = "//div[@class='VizExIcon__IconWrapper-vk957b-0 cnIHbO']"

    def entity_name(self, entityname):
        self.driver.find_element(By.XPATH, self.Entity_Name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Entity_Name_xpath).send_keys(entityname)

    def state(self):
        self.select = Select(self.driver.find_element(By.NAME, self.State_name))
        self.select.select_by_visible_text("California")

    def formation(self, formation):
        self.driver.find_element(By.XPATH, self.Formation_xpath).clear()
        self.driver.find_element(By.XPATH, self.Formation_xpath).send_keys(formation)

    def entity_number(self, entity_number):
        self.driver.find_element(By.XPATH, self.Entity_Number_xpath).clear()
        self.driver.find_element(By.XPATH, self.Entity_Number_xpath).send_keys(entity_number)

    def entity_type(self):
        self.select = Select(self.driver.find_element(By.NAME, self.Entity_Type_name))
        self.select.select_by_visible_text("LLC")

    def chat_button(self):
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH, self.chat_xpath).click()
        self.driver.switch_to.default_content()

    def next(self):

        self.driver.find_element(By.XPATH, self.Next_Button_xpath).click()
