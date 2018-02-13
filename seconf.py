# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from user import User


class Seconf(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_seconf(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_new(driver)
        self.crate_and_submit(driver, User(name= "asdasd", last_name= "dfsfds", nick_name= "asdfsd"))
        self.home_page(driver)

    def test_second_empty(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_new(driver)
        self.crate_and_submit(driver, User(name= "name", last_name= "last", nick_name= "nick"))
        self.home_page(driver)

    def home_page(self, driver):
        print("Open home page")
        driver.find_element_by_link_text("home page").click()

    def crate_and_submit(self, driver, user):
        print("Add user and submit")
        # fill form
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(user.name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(user.last_name)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(user.nick_name)
        # submit creatiion
        submitBtn = driver.find_element_by_xpath("//*[@name='submit']")
        submitBtn.click()

    def open_new(self, driver):
        print("Go to add new user page")
        driver.find_element_by_link_text(u"add new").click()

    def login(self, driver, username, password):
        print("Login actions")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, driver):
        print("Open home page")
        driver.get(self.base_url + "addressbook/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
