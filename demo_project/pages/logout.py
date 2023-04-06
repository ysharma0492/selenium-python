from demo_project.Locators.locator import Locators
class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button_xpath ="//header/div[1]/div[2]/ul[1]/li[1]/span[1]/i[1]"
        self.click_logout_link_text = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[1]/ul[1]/li[4]/a[1]"

    def click_menu(self):
        self.driver.find_element("xpath", self.menu_button_xpath).click()

    def click_logout(self):
        self.driver.find_element("xpath", self.click_logout_link_text).click()
