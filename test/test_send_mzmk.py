import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_send_mzmk(msk_login, browser):
    # Создать МЗМК и отправить его в МСК через эмулятор
    # Войти в МСК через браузер
    msk_login
    # Кнопка Заявления -- //*[@id="button-2397-btnIconEl"]
    # button_claim = browser.find_element_by_xpath("//*[@id='button-2397-btnIconEl']")
    # button_claim.click()
    # Поле СНИЛС -- //*[@id="textfield-1029-inputEl"]
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.NAME, "snils"))
    )
    input_snils = browser.find_element_by_name("snils")
    snils = "764-099-239 39"
    input_snils.send_keys(snils)
    # WebDriverWait(browser, 3)
    # Кнопка Применить -- //*[@id="button-1053-btnIconEl"]
    button_apply = browser.find_element_by_xpath("//*[@id='button-1053-btnIconEl']")
    button_apply.click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{snils}']"))
    )
    row_found = browser.find_element_by_xpath(f"//*[text()='{snils}']")
    row_found.click()
    link_show = browser.find_element_by_xpath("//*[@id='linkButton-1058-btnEl']")
    link_show.click()
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element_value((By.XPATH, "//*[@id='citizenSnils-inputEl']"), snils)
    )
    link_decision = browser.find_element_by_xpath("//span/span/span[text()='Решение']")
    link_decision.click()
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Тип решения:']"))
    )
    button_edit = browser.find_element_by_xpath("//*[text()='Редактировать решение']")
    button_edit.click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Тип решения']"))
    )
    type_decision = browser.find_element_by_xpath("//label[text()='Тип решения']/ancestor::tr/td[2]/table")
    type_decision.click()
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.XPATH, "//li[text()='ОТКАЗАТЬ']"))
    )
    # Цикл против selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
    staleElement = True
    while(staleElement):
        try:
            browser.find_element_by_xpath("//li[text()='УДОВЛЕТВОРИТЬ']").click()
            staleElement = False
        except StaleElementReferenceException:
            staleElement = True

    time.sleep(10)
