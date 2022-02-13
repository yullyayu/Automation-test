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

def test_register(driver):
    filename = time.strftime("%Y_%m_%d_%H%M%S")
    driver.save_screenshot("E:/website-test/Screenshots/Register/1."+filename+".png")
    driver.find_element(By.XPATH,'//p[@class="pr-4 sigil-header__nav-action bl-text bl-text--body-small bl-text--semi-bold"]').click()
    driver.find_element(By.XPATH,'//input[@class="bl-text-field__input"]').send_keys('yullyayu@gmail.com')
    driver.save_screenshot("E:/website-test/Screenshots/Register/2."+filename+".png")
    time.sleep(3)
    driver.find_element(By.XPATH,'//button[@class="bl-button bl-button--primary bl-button--medium bl-button--block"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Register/3."+filename+".png")
    driver.find_element(By.XPATH,'//span[@class="bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse"]').click()
    driver.save_screenshot("E:/website-test/Screenshots/Register/4."+filename+".png")
    time.sleep(20)
    driver.find_element(By.XPATH,'//span[@class="bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse"]').click()
    driver.save_screenshot("E:/website-test/Screenshots/Register/5."+filename+".png")
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@class="bl-text-field__input"]').click()
    driver.save_screenshot("E:/website-test/Screenshots/Register/6."+filename+".png")
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[@class="mb-128 bl-button bl-button--primary bl-button--medium bl-button--block"]').click()
    driver.save_screenshot("E:/website-test/Screenshots/Register/7."+filename+".png")

    #Berhasil buat akun Lanjut
    time.sleep(5)
    driver.find_element(By.XPATH,'//span[@class="bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse"]').click()
    driver.save_screenshot("E:/website-test/Screenshots/Register/8."+filename+".png")

