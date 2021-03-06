from pages.locators.log_in_out_page_locators import LogInOutPageLocators
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver  # type: WebDriver
        self.app.open_home_page()
        print("Login actions")

        user_name_element = driver.find_element_by_name("user")  # type: WebElement
        user_name_element.clear()
        user_name_element.send_keys(username)

        password_element = driver.find_element_by_name("pass")  # type: WebElement
        password_element.clear()
        password_element.send_keys(password)
        driver.find_element_by_xpath(LogInOutPageLocators.LOGIN_BTN).click()

    def ensure_login(self, username, password):
        if self.is_loged_in():
            if self.is_loged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        print("Log out")
        driver = self.app.driver
        logOutBtn = driver.find_element_by_xpath(LogInOutPageLocators.LOGOUT_BTN)  # type: WebElement
        logOutBtn.click()

    def ensure_logout(self):
        if self.is_loged_in():
            self.logout()

    def is_loged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath(LogInOutPageLocators.LOGOUT_BTN)) > 0

    def is_loged_in_as(self, username):
        return username in self.get_logged_username()

    def get_logged_username(self):
        driver = self.app.driver
        return driver.find_element_by_xpath(LogInOutPageLocators.USER_NAME).text[1:-1]
