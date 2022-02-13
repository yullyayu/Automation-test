from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.bukalapak.com/')
    time.sleep(5)
    yield driver
    driver.quit()

def test_login(driver):
    filename = time.strftime("%Y_%m_%d_%H%M%S")
    driver.save_screenshot("E:/website-test/Screenshots/Login/1."+filename+".png")
    driver.find_element(By.XPATH,'//a[@class="sigil-header__nav te-header-login"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Login/2."+filename+".png")
    driver.find_element(By.XPATH,'//input[@id="LoginID"]').send_keys('083144438988')
    driver.save_screenshot("E:/website-test/Screenshots/Login"+filename+".png")
    driver.find_element(By.XPATH,'//span[@class="bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse"]').click()
    time.sleep(20)
    driver.save_screenshot("E:/website-test/Screenshots/Login/3."+filename+".png")
    #time for input otp manual
    driver.find_element(By.XPATH,'//button[@class="bl-button bl-button--primary bl-button--medium bl-button--block"]').click()
    driver.save_screenshot("E:/website-test/Screenshots/Login/4"+filename+".png")
