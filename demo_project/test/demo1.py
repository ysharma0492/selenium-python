import time
import unittest
from selenium import webdriver
from demo_project.pages.login import LoginPage
from demo_project.pages.logout import Logout


class Googlesearch(unittest.TestCase):

    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:/Users/yogesh.sharma/Downloads/chromedriver_win32 (1).exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(2)

    def test_logout(self):
        driver = self.driver
        logout = Logout(driver)
        logout.click_menu()
        time.sleep(3)
        logout.click_logout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

# if __name__ == '__main__':
# unittest.main()
