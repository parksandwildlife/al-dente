"""An example testing script."""

# import argparse
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
import os
import unittest

# Read config
load_dotenv(find_dotenv())


class LearningTest(unittest.TestCase):
    """A base TestCase for DBCA's training portal."""

    def login(self, driver):
        """Return a logged in driver."""
        driver.get(os.environ.get("COURSE"))
        assert "Log in to the site" in driver.title
        assert "Log in" in driver.title
        driver.find_element_by_name("username").send_keys(os.environ.get("UN"))
        driver.find_element_by_name("password").send_keys(os.environ.get("PW"))
        driver.find_element_by_name("rememberusername").click()
        driver.find_element_by_id("loginbtn").click()
        assert "You are logged in as" in driver.page_source
        return driver

    def setUp(self):
        """Return logged in drivers for Chrome and Firefox."""
        self.chrome = self.login(webdriver.Chrome('./drivers/chromedriver'))
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = True
        self.firefox = self.login(webdriver.Firefox(profile))
        # remote:
        # bs_url = 'http://{0}:{1}@hub.browserstack.com:80/wd/hub'.format(
        #     env(REMOTE_UN), env(REMOTE_PW)
        # driver = webdriver.Remote(
        #   command_executor=bs_url,
        #   desired_capabilities={
        #       'browser': 'chrome',
        #       'build': 'First build',
        #       'browserstack.debug': 'true'
        #   })

    def test_logged_in(self):
        """Test whether the setUp method works.

        The setUp should log the user into the course landing page.
        """
        print("Test whether user can log in and gets to landing page.")
        self.chrome.save_screenshot('results/chrome_logged_in.png')
        self.firefox.save_screenshot('results/firefox_logged_in.png')
        assert "You are logged in as" in self.chrome.page_source
        assert "You are logged in as" in self.firefox.page_source

    def tearDown(self):
        """TearDown: close webdriver."""
        self.chrome.close()
        self.firefox.close()
        pass

if __name__ == "__main__":
    unittest.main()
