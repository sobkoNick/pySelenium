class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        print("Login actions")

        user_name_element = driver.find_element_by_name("user")
        user_name_element.clear()
        user_name_element.send_keys(username)

        password_element = driver.find_element_by_name("pass")
        password_element.clear()
        password_element.send_keys(password)

        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        print("Log out")
        driver = self.app.driver
        logOutBtn = driver.find_element_by_xpath("//*[@name='logout']/a")
        logOutBtn.click()
