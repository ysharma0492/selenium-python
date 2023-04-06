from demo_project.Locators.locator import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_id = Locators.login_id

    def enter_username(self, username):
        self.driver.find_element("name", Locators.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("name", Locators.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element("xpath", Locators.login_id).click()
