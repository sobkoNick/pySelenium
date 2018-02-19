from selenium import webdriver

from constants import Constants
from pages.session import SessionHelper
from pages.user_page import UserHelper


class Application:
    def __init__(self, browser, project_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome(Constants.WEB_DRIVER_WAY)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.implicitly_wait(1)
        self.base_url = Constants.BASE_URL
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)  # reference to SessionHelper which has login() method
        self.user_helper = UserHelper(self)
        self.project_url = project_url

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        print("Open home page")
        driver.get(self.base_url + self.project_url)

    def destroy(self):
        self.driver.quit()
