import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test053001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardDown(self):
        self.driver.quit()

    def test_041401(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(616, 778)
        self.driver.find_element(By.ID, "kw").send_keys("秦牛正威")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(8)


if __name__ == "__main__":
    unittest.main()
