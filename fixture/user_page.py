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
        self.fill_form(user)
        # submit creation
        submitBtn = driver.find_element_by_xpath("//*[@name='submit']")
        submitBtn.click()

    def fill_form(self, user):
        # fill form
        self.type_text_to_element("firstname", user.name)
        self.type_text_to_element("lastname", user.last_name)
        self.type_text_to_element("nickname", user.nick_name)

    def type_text_to_element(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            element = driver.find_element_by_name(field_name);
            element.clear()
            element.send_keys(text)

    def delete_first_user(self):
        print("Delete first user")
        driver = self.app.driver
        self.select_first()
        delete_btn = driver.find_element_by_xpath("//*[@value='Delete']")
        delete_btn.click()

        alert = Alert(driver)
        alert.accept()

    def select_first(self):
        driver = self.app.driver
        first_checkbox = driver.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[1]")
        first_checkbox.click()

    def modify(self, modify_data):
        driver = self.app.driver
        self.select_first()
        # open modification form
        modify_first_brt = driver.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]")
        modify_first_brt.click()
        self.fill_form(modify_data)
        update_btn = driver.find_element_by_name("update")
        update_btn.click()
        self.back_to_home_page()

    def back_to_home_page(self):
        driver = self.app.driver
        print("Open home page")
        driver.find_element_by_link_text("home").click()
