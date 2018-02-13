from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from fixture.session import SessionHelper
from fixture.add_new import AddHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)  # reference to SessionHelper which has login() method
        self.add_new = AddHelper(self)

    def open_home_page(self):
        driver = self.driver
        print("Open home page")
        driver.get(self.base_url + "addressbook/")

    def destroy(self):
        self.driver.quit()
