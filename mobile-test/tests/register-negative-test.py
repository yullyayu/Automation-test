import os, sys
import glob
import unittest
import time
from unittest import suite
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

class RegisterTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'vivo 1724'
        desired_caps['appPackage'] = 'com.loginmodule.learning'
        desired_caps['appActivity'] = 'com.loginmodule.learning.activities.LoginActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    
    """
    Scenario Test: Registrasi pengguna, ketika konfirmasi password tidak sesuai

    """
    def case1(self):   
        print("Scenario Test: Registrasi pengguna, ketika konfirmasi password tidak sesuai")  
        #take screenshots
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname+ts
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textViewLinkRegister').click()
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/1.1"+filename+".png")

        time.sleep(3)
        #name
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextName').send_keys('yully ayu')
        #email
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextEmail').send_keys('yullyayu@gmail.com')
        #password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextPassword').send_keys('123456')
        #confirm password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextConfirmPassword').send_keys('654321')

        time.sleep(3)
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/1.2."+filename+".png")

        touch = TouchAction(self.driver)
        touch.press(x=327, y=1200).move_to(x=334, y=967).release().perform()
        #Register
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/appCompatButtonRegister').click()	
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/1.3."+filename+".png")
        self.driver.start_activity("com.loginmodule.learning", "com.loginmodule.learning.activities.LoginActivity")


    """
    Scenario Test: Registrasi pengguna, ketika field "Name" dikosongkan

    """
    def case2(self):     
        print("Scenario Test: Registrasi pengguna, ketika field Name dikosongkan")
        #take screenshots
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname+ts
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textViewLinkRegister').click()
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/2.1."+filename+".png")

        time.sleep(3)
        #name
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextName').send_keys('')
        #email
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextEmail').send_keys('yullyayu@gmail.com')
        #password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextPassword').send_keys('123456')
        #confirm password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextConfirmPassword').send_keys('123456')

        time.sleep(3)
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/2.2."+filename+".png")

        touch = TouchAction(self.driver)
        touch.press(x=327, y=1200).move_to(x=334, y=967).release().perform()
        #Register
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/appCompatButtonRegister').click()	
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/2.3."+filename+".png")
        self.driver.start_activity("com.loginmodule.learning", "com.loginmodule.learning.activities.LoginActivity")

    """
    Scenario Test: Registrasi pengguna, ketika invalid Email

    """
    def case3(self):     
        print("Scenario Test: Registrasi pengguna, ketika invalid Email")
        #take screenshots
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname+ts
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textViewLinkRegister').click()
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/3.1."+filename+".png")

        time.sleep(3)
        #name
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextName').send_keys('Yully ayu')
        #email
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextEmail').send_keys('yullyayu')
        #password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextPassword').send_keys('123456')
        #confirm password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextConfirmPassword').send_keys('123456')

        time.sleep(3)
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/3.2."+filename+".png")

        touch = TouchAction(self.driver)
        touch.press(x=327, y=1200).move_to(x=334, y=967).release().perform()
        #Register
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/appCompatButtonRegister').click()	
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Negative/3.3."+filename+".png")
        self.driver.start_activity("com.loginmodule.learning", "com.loginmodule.learning.activities.LoginActivity")
    
    def testCase(self):
        self.case1()
        self.case2()
        self.case3()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    unittest.TextTestRunner(verbosity=3).run(suite)

    