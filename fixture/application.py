from selenium import webdriver

from fixture.session import SessionHelper
from fixture.user_page import UserHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/MykolaSobko/PycharmProjects/pySelenium/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)  # reference to SessionHelper which has login() method
        self.user_helper = UserHelper(self)

    def open_home_page(self):
        driver = self.driver
        print("Open home page")
        driver.get(self.base_url + "addressbook/")

    def destroy(self):
        self.driver.quit()
