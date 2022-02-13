import unittest
import time
from unittest import suite
from appium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'vivo 1724'
        desired_caps['appPackage'] = 'com.loginmodule.learning'
        desired_caps['appActivity'] = 'com.loginmodule.learning.activities.LoginActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def case1(self):   
        print("Scenario Test: Login pengguna, ketika inputan tidak sesuai")
        #take screenshots
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname+ts

        self.driver.save_screenshot("E:/mobile-test/Screenshots/Login/1"+filename+".png")

        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextEmail').send_keys('ayu2@gmail.com')
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextPassword').send_keys('123456')
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Login/2"+filename+".png")
        time.sleep(2)
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/appCompatButtonLogin').click()
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Login/3"+filename+".png")

    def testCase(self):
        self.case1()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=3).run(suite)