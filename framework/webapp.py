from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebApp():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_driver(self):
        return self.driver


webapp = WebApp.get_instance()
