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

    """
    Scenario: Login
    """
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/1."+filename+".png")
    driver.find_element(By.XPATH,'//a[@class="sigil-header__nav te-header-login"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/2."+filename+".png")
    driver.find_element(By.XPATH,'//input[@id="LoginID"]').send_keys('muzdalifahyully@gmail.com')
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/3."+filename+".png")
    driver.find_element(By.XPATH,'//span[@class="bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/4."+filename+".png")
    driver.find_element(By.XPATH,'//input[@id="Password"]').send_keys('08Juli1998')
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/5."+filename+".png")
    driver.find_element(By.XPATH,'//button[@id="btn-login"]').click()
    time.sleep(5)

    """
    Scenario test: Add to cart
    """
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/6."+filename+".png")
    driver.execute_script("window.scrollBy(0,500)","")
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/6."+filename+".png")
    driver.find_element(By.XPATH,'//div[@class="bl-image-group__head"]').click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,500)","")
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/7."+filename+".png")
    driver.find_element(By.XPATH,'//img[@class="image"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/8."+filename+".png")
    driver.execute_script("window.scrollBy(0,500)","")
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/9."+filename+".png")
    driver.find_element(By.XPATH,'//button[@class="c-main-product__action__cart bl-button bl-button--outline bl-button--medium"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/10."+filename+".png")
    driver.find_element(By.XPATH,'//button[@class="c-cart-dialog__cart-button c-btn c-btn--default c-btn--default c-btn--default"]').click()
    time.sleep(3)
    driver.save_screenshot("E:/website-test/Screenshots/Add to Cart/11."+filename+".png")