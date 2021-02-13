import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
# import math


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_login(browser):
    browser.get("https://mini-ecasa/mskt/index")
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    submit = browser.find_element_by_class_name("formButton")
    username.send_keys("msk_auto")
    password.send_keys("1Qaz2Wsx")
    submit.click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.NAME, "orgUnit"))
    )
    chooseTO = browser.find_element_by_name("orgUnit")
    submit = browser.find_element_by_xpath("//input[@type='submit']")
    submit.click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "btnChangeOrgUnit-btnIconEl"))
    )
    print(">>>>>>>> logged in")



