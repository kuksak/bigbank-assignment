from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.webapp import webapp


class LoanPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoanPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.driver_wait = WebDriverWait(self.driver, 1000)

    def load_page(self):
        self.driver.get("https://ansokan.bigbank.se/")

    def find_element_by_id(self, element_id):
        return self.driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, element_id)))

    def find_element_by_xpath(self, xpath):
        return self.driver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def find_element_by_name(self, name):
        return self.driver_wait.until(expected_conditions.visibility_of_element_located((By.NAME, name)))


loan_page = LoanPage.get_instance()
