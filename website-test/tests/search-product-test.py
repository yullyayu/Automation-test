from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.bukalapak.com/')
    time.sleep(5)
    yield driver
    driver.quit()

def test_search_product(driver):
    filename = time.strftime("%Y_%m_%d_%H%M%S")
    driver.save_screenshot("E:/website-test/Screenshots/Search Product/1."+filename+".png")
    driver.find_element(By.XPATH,'//input[@name="search[keywords]"]').send_keys('Kulkas' + Keys.ENTER)
    time.sleep(5)
    driver.save_screenshot("E:/website-test/Screenshots/Search Product/2."+filename+".png")
