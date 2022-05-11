from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import pytest

options = webdriver.FirefoxOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.add_argument("--disable-blink-features=AutomationControlled")


url = "http://suninjuly.github.io/simple_form_find_task.html"

driver = webdriver.Chrome(executable_path='SET PATH FOR DRIVER ',
                          options=options)


# filling form
def filling():
    try:
        driver.get(url=url)
        time.sleep(10)

        search_input= driver.find_element(by=By.NAME, value='first_name')
        search_input.send_keys('My name is  Slim Shady')

        search_input = driver.find_element(by=By.NAME, value='last_name')
        search_input.send_keys('The real Slim Shady')

        search_input = driver.find_element(by=By.NAME, value='firstname')
        search_input.send_keys('Detroit')

        search_input = driver.find_element(by=By.ID, value='country')
        search_input.send_keys('USA')

        search_input = driver.driver.find_element(by=By.ID, value='submit_button')
        search_input.click()

        alert = driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        time.sleep(2)
        alert.accept()

        time.sleep(2)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()
filling()
