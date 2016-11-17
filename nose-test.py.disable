import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class GithubSearchTest(unittest.TestCase):

    def setUp(self):
    	self.driver = webdriver.PhantomJS()
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.base_url = "http://8bitrockr.com/"


    def test_01(self):
        driver = self.driver
        driver.get(self.base_url)
        print driver.page_source
        assert "NFQ" in driver.page_source

    def test_02(self):
        driver = self.driver
        driver.get(self.base_url)
        assert "global" in driver.page_source

    def test_03(self):
        driver = self.driver
        driver.get(self.base_url)
        assert "global" in driver.page_source

    def tearDown(self):
        self.driver.close()
