class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        print("Login actions")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        print("Log out")
        driver = self.app.driver
        logOutBtn = driver.find_element_by_xpath("//*[@name='logout']/a")
        logOutBtn.click()
