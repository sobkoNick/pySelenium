from selenium.webdriver.common.alert import Alert


class UserHelper:
    def __init__(self, app):
        self.app = app

    def open_new(self):
        driver = self.app.driver
        print("Go to add new user page")
        driver.find_element_by_link_text(u"add new").click()

    def crate_and_submit(self, user):
        driver = self.app.driver
        self.open_new()
        print("Add user and submit")
        # fill form
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(user.name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(user.last_name)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(user.nick_name)
        # submit creation
        submitBtn = driver.find_element_by_xpath("//*[@name='submit']")
        submitBtn.click()

    def delete_first_user(self):
        print("Delete first user")
        driver = self.app.driver
        first_checkbox = driver.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[1]")
        first_checkbox.click()
        delete_btn = driver.find_element_by_xpath("//*[@value='Delete']")
        delete_btn.click()

        alert = Alert(driver)
        alert.accept()

        # self.back_to_home_page()

    def back_to_home_page(self):
        driver = self.app.driver
        print("Open home page")
        driver.find_element_by_link_text("home page").click()
