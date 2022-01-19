from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from POMDemo.Pages.DetailPage import DetailPage
from POMDemo.Pages.Setupfiling import Setup
from POMDemo.Pages.EntityProfile import Entity
from POMDemo.Pages.AdditionalJurisdictions import Jurisdiction
from POMDemo.Pages.PlanDetail import PlanDetail


class Onboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(25)

    def test_input_details(self):
        driver = self.driver
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--incognito")
        #driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()
        driver.get("http://13.64.144.136/qa/onboarding")
        detail = DetailPage(driver)
        setup = Setup(driver)
        entity = Entity(driver)
        jurisdiction = Jurisdiction(driver)
        plan = PlanDetail(driver)

        detail.get_started()
        detail.enter_name("FileJet")
        detail.enter_phone("9659450001")
        detail.enter_email("filejet@filejet.com")
        detail.enter_company("FileJet")
        detail.enter_industry()
        detail.enter_entities("2")
        detail.enter_jurisdiction("3")
        detail.enter_intention()
        detail.enter_password("123456")
        detail.enter_confirm_password("123456")
        #detail.chat_button()
        detail.button_next()
        #setup.i_got()
        #setup.next()
        entity.entity_name("FileJet")
        entity.state()
        entity.formation("01/05/2022")
        entity.entity_number("202265555")
        entity.entity_type()
        entity.next()
        jurisdiction.jurisdiction()
        jurisdiction.add()
        jurisdiction.entityname("Apple Inc")
        jurisdiction.state()
        jurisdiction.formation_date("02/10/2022")
        jurisdiction.jurisdiction_number("963695")
        jurisdiction.entity_type()
        jurisdiction.next()
        plan.annual()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
