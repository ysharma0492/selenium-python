from selenium import webdriver
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/yogesh.sharma/Downloads/chromedriver_win32 (1).exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test pass")


def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element("name", "username").send_keys("Admin")
    driver.find_element("name", "password").send_keys("admin123")
    driver.find_element("xpath", "//button[@type='submit']").click()