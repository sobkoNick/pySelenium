import re

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from model.user import User
from pages.locators.user_page_locators import UserPageLocators
import time


class UserHelper:
    def __init__(self, app):
        self.app = app

    def open_new(self):
        driver = self.app.driver
        print("Go to add new user page")
        driver.find_element_by_link_text(u"add new").click()

    def create_and_submit(self, user):
        driver = self.app.driver
        self.open_new()
        print("Add user and submit")
        self.fill_form(user)
        # submit creation
        submitBtn = driver.find_element_by_xpath(UserPageLocators.SUBMIT_BTN)
        submitBtn.click()
        self.user_cache = None

    def fill_form(self, user):
        # fill form
        self.type_text_to_element("firstname", user.name)
        self.type_text_to_element("lastname", user.last_name)
        self.type_text_to_element("nickname", user.nick_name)

    def type_text_to_element(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            element = driver.find_element_by_name(field_name)
            element.clear()
            element.send_keys(text)

    def delete_user(self, index):
        print("Delete first user")
        driver = self.app.driver
        self.select_user_by_index(index)
        delete_btn = driver.find_element_by_xpath(UserPageLocators.DELETE_BTN)
        delete_btn.click()
        alert = Alert(driver)
        alert.accept()
        self.user_cache = None

    def select_user_by_index(self, index):
        driver = self.app.driver
        checkbox = driver.find_elements_by_xpath(UserPageLocators.CHECKBOXES_IN_TABLE)[index]
        checkbox.click()

    def modify_user(self, modify_data, index):
        driver = self.app.driver
        self.open_user_edit_page(index)
        self.fill_form(modify_data)
        update_btn = driver.find_element_by_name("update")
        update_btn.click()
        self.go_to_home_page()
        self.user_cache = None

    def open_user_edit_page(self, index):
        driver = self.app.driver
        modify_btn = driver.find_elements_by_xpath(UserPageLocators.MODIFY_BUTTONS_IN_TABLE)[index]
        modify_btn.click()

    def open_user_to_view_details(self, index):
        driver = self.app.driver
        view_btn = driver.find_elements_by_xpath(UserPageLocators.VIEW_BUTTONS_IN_TABLE)[index]  # type: WebElement
        view_btn.click()

    def go_to_home_page(self):
        driver = self.app.driver
        if not driver.current_url.endswith('addressbook/'):
            print("Open home page")
            driver.find_element_by_link_text("home").click()
        time.sleep(3)  # driver searches for elements too soon

    def count(self):
        driver = self.app.driver
        self.go_to_home_page()
        return self.get_table_lenght(driver)

    def get_table_lenght(self, driver):
        return len(driver.find_elements_by_xpath(UserPageLocators.TABLE_ROWS))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            driver = self.app.driver
            # self.go_to_home_page()
            self.user_cache = []
            for element in driver.find_elements_by_xpath(UserPageLocators.TABLE_ROWS):
                name = element.find_element_by_xpath("./td[3]").text  # './' - locates element from parent
                id = element.find_element_by_xpath("./td[1]/input").get_attribute("value")
                all_phones = element.find_element_by_xpath("./td[6]").text
                self.user_cache.append(User(name=name, id=id, all_phones_from_home_page=all_phones))

            return list(self.user_cache)

    def get_contact_from_edit_page(self, index):
        driver = self.app.driver
        self.open_user_edit_page(index)
        name = driver.find_element_by_name("firstname").get_attribute("value")
        last_name = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        home_phone = driver.find_element_by_name("home").get_attribute("value")
        mobile_phone = driver.find_element_by_name("mobile").get_attribute("value")
        work_phone = driver.find_element_by_name("work").get_attribute("value")
        return User(name=name, last_name=last_name, nick_name=None, id=id, home_phone=home_phone,
                    mobile_phone=mobile_phone, work_phone=work_phone)

    def get_user_from_view_page(self, index):
        driver = self.app.driver  # type: WebDriver
        self.open_user_to_view_details(index)
        text = driver.find_element_by_id("content").text
        homePhone = re.search("H: (.*)", text).group(1)
        workPhone = re.search("W: (.*)", text).group(1)
        mobilePhone = re.search("M: (.*)", text).group(1)
        return User(home_phone=homePhone, mobile_phone=mobilePhone, work_phone=workPhone)
