from selenium.webdriver.support.wait import WebDriverWait

from framework.webapp import webapp


class CalculatorModal():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CalculatorModal()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def load_modal(self):
        self.driver.get("https://ansokan.bigbank.se/")
        ##  additional click to go to the next calculator modal dialog box
        self.driver.find_element_by_class_name('bb-edit-amount').click()
        self.driver_wait = WebDriverWait(self.driver, 1000)

    def find_elements_by_class(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)


calculator_modal = CalculatorModal.get_instance()
