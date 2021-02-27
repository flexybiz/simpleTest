import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_send_mzmk(msk_login, browser):
    # Создать МЗМК и отправить его в МСК через эмулятор
    # Войти в МСК через браузер
    msk_login
#Кнопка Заявления -- //*[@id="button-2397-btnIconEl"]
#Поле СНИЛС -- //*[@id="textfield-1029-inputEl"]
#Кнопка Применить -- //*[@id="button-1053-btnIconEl"]
    button_claim = browser.find_element_by_xpath("//*[@id='button-2397-btnIconEl']")
    button_claim.click()
    input_snils = browser.find_element_by_name("snils")
    snils = "764-099-239 39"
    input_snils.send_keys(snils)
    WebDriverWait(browser, 3)
    button_apply = browser.find_element_by_xpath("//*[@id='button-1053-btnIconEl']")
    button_apply.click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//*[text()='{snils}']"))
    )
    row_found = browser.find_element_by_xpath(f"//*[text()='{snils}']")
    row_found.click()
    link_show = browser.find_element_by_xpath("//*[@id='linkButton-1058-btnEl']")
    link_show.click()
    time.sleep(10)

    time.sleep(10)
