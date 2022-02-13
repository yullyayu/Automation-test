import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

class RegisterPositiveTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'vivo 1724'
        desired_caps['appPackage'] = 'com.loginmodule.learning'
        desired_caps['appActivity'] = 'com.loginmodule.learning.activities.LoginActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    """
        Scenario Test: Registrasi pengguna berhasil

    """
    def case1(self): 
        #take screenshots
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        activityname = self.driver.current_activity
        filename = activityname+ts

        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textViewLinkRegister').click()
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Positive/1.positive"+filename+".png")

        time.sleep(3)
        #name
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextName').send_keys('alifah ayu')
        #email
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextEmail').send_keys('alifah@gmail.com')
        #password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextPassword').send_keys('a12345')
        #confirm password
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/textInputEditTextConfirmPassword').send_keys('a12345')

        time.sleep(3)
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Positive/2.positive"+filename+".png")

        touch = TouchAction(self.driver)
        touch.press(x=327, y=1200)
        touch.move_to(x=334, y=967)
        touch.release()
        touch.perform()
        #Register
        self.driver.find_element(By.ID,'com.loginmodule.learning:id/appCompatButtonRegister').click()	
        self.driver.save_screenshot("E:/mobile-test/Screenshots/Register/Positive/3.positive"+filename+".png")

    def testCase(self):
        self.case1()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterPositiveTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
