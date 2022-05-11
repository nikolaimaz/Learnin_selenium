from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import pytest

options = webdriver.FirefoxOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

options.add_argument("--disable-blink-features=AutomationControlled")


url = "https://mikolai-mazurek.tk/"

driver = webdriver.Firefox(service=Service('/home/nikolai/PycharmProjects/test/geckodriver'),
                          options=options)


# filling form

def test():
    try:
        driver.get(url=url)
        time.sleep(1)

        search_input= driver.find_element(by=By.NAME, value='name')
        search_input.send_keys('My name is  Slim Shady')
        print('done')




        search_input = driver.find_element(by=By.ID, value='message')
        search_input.send_keys('Detroit')
        print('done')




    except Exception as ex:
        print(ex)

    finally:
        time.sleep(10)
        driver.close()
        driver.quit()
test()
