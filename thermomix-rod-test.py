# Pick a day that has no recipe associated with it yet

# https://docs.google.com/spreadsheets/d/1AHyJ2aWdg186lnUNd6QYUEr0Xi2WCvexcSBmHZ9JTY4/edit#gid=0
# Test case ID: DAIL1
# Test Author: Chi Nguyen
# Objective: Check function pick recipe of the day with a condition where the day has no recipe of the day yet
# Prerequisites: a moderator account, a recipe 

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ThermomixTest(unittest.TestCase):

    def setUp(self):
    	#self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        #self.base_url = "http://v3.viet-staging.community.thermomix.com/"
        self.base_url = "http://v3.viet-staging.community.thermomix.com/"

    def test_01(self):
        driver = self.driver
        driver.get(self.base_url)
        #print driver.page_source
        #assert "NFQ" in driver.page_source

        # Admin login with username=chi-2015, password=chi-2015
        username = driver.find_element_by_id('loginUsername')
        username.send_keys('modvn')

        password = driver.find_element_by_id('loginPassword')
        password.send_keys('modvn')

        form = driver.find_element_by_id('tmrc_login_form')
        form.submit()

        # Go to 1 recipe (none of the day feature)
        driver.implicitly_wait(100)
        driver.get("http://v3.viet-staging.community.thermomix.com/baking-savoury-recipes/variation-summer-quinoa-bites/wgx10gtt-c4ca4-851640-cfcd2-t7b2fc0p")

        # Scroll down at the bottom
        driver.implicitly_wait(100)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        driver.implicitly_wait(100)

        # Click on datepicker
        element = driver.find_element_by_xpath("/html/body/div[2]/div/div/article/div/div[2]/div/section[1]/div/div[4]/div/div/form/div[1]/div/input")
        element.click()
        driver.implicitly_wait(300)

        # assert "NFQ" in driver.page_source
        time.sleep(60)
        driver.quit()

    def tearDown(self):
        self.driver.close()
