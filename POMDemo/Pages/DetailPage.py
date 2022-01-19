from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DetailPage():

    def __init__(self, driver):
        self.wait = None
        self.select = None
        self.driver = driver

        #self.get_started_button_xpath = "//button[@type='submit']"
        self.get_started_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        self.name_textbox_class_name = "form-control"
        self.phone_textbox_name = "phone"
        self.email_textbox_name = "email"
        self.company_xpath = "//input[@name='company']"
        self.industry_xpath = "//select[@name='industry']"
        self.entities_xpath = "//input[@name='total_entities']"
        self.jurisdiction_name = "total_jurisdictions"
        self.intention_xpath = "//select[@name='purpose']"
        self.password_id = "password"
        self.confirm_password_id = "password-confirm"
        self.next_button_xpath = "//button[@class='btn btn-primary next']"
        self.chat_xpath = "//button[@class='InitialMessageBubble__CloseButton-sc-1g1lbsw-2 cogBem']"

    def get_started(self):
        self.get_started_button.click()
        #self.driver.find_element_by_xpath(self.get_started_button_xpath).click() //TEST

    def chat_button(self):
        self.driver.find_element_by_xpath(self.chat_xpath).click()

    def enter_name(self, name):
        self.driver.find_element_by_class_name(self.name_textbox_class_name).send_keys(name)

    def enter_phone(self, phone):
        self.driver.find_element_by_name(self.phone_textbox_name).send_keys(phone)

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

    def enter_company(self, company):
        self.driver.find_element_by_xpath(self.company_xpath).send_keys(company)

    def enter_industry(self):
        self.select = Select(self.driver.find_element_by_xpath(self.industry_xpath))
        self.select.select_by_visible_text("Education")

    def enter_entities(self, entities):
        self.driver.find_element_by_xpath(self.entities_xpath).send_keys(entities)

    def enter_jurisdiction(self, jurisdiction):
        self.driver.find_element_by_name(self.jurisdiction_name).send_keys(jurisdiction)

    def enter_intention(self):
        self.select = Select(self.driver.find_element_by_xpath(self.intention_xpath))
        self.select.select_by_visible_text("Entity Formations")

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element_by_id(self.confirm_password_id).send_keys(confirm_password)

    def button_next(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.find_element_by_xpath(self.next_button_xpath).click()

    # def chat_button1(self):
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "InitialMessageBubble__CloseButton-sc-6igoo2-2 jqVklV")))
    #     self.driver.find_element_by_xpath(self.chat_xpath).click()
