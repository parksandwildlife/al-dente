"""An example testing script."""

# import argparse
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
import os
import unittest

# Read config
load_dotenv(find_dotenv())


# ---------------------------------------------------------------------------#
# Main test class defining all test cases
# ---------------------------------------------------------------------------#
class LearningTest(unittest.TestCase):
    """A base TestCase for DBCA's training portal using Chrome."""

    drivername = "chrome"

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
        # Chrome
        self.driver = self.login(webdriver.Chrome())

        # Local driver - required setup for TravisCI
        # from selenium.webdriver.chrome import service as chrome_service
        # self.service = chrome_service.Service('/usr/local/bin/chromedriver')
        # self.service.start()
        # capabilities = {'chrome.binary': '/usr/bin/google-chrome-stable'}
        # self.ls = webdriver.Remote(self.service.service_url, capabilities)

        # Browserstack remote driver
        # bs_url = 'http://{0}:{1}@hub.browserstack.com:80/wd/hub'.format(
        #     os.environ.get("REMOTE_UN"), os.environ.get("REMOTE_PW"))
        # self.rd = webdriver.Remote(
        #     command_executor=bs_url,
        #     desired_capabilities={
        #         'browser': 'chrome',
        #         'build': 'First build',
        #         'browserstack.debug': 'true'
        #     }
        # )

    def test_logged_in(self):
        """Test if the user can log in.

        If logged in, the menu bar shows "Logged in as...".
        """
        self.driver.save_screenshot(
            'results/{0}_logged_in.png'.format(self.drivername))
        assert "You are logged in as" in self.driver.page_source

    def tearDown(self):
        """TearDown: close webdriver."""
        self.driver.close()


# ---------------------------------------------------------------------------#
# Alternative browser engines: add one class per engine
# ---------------------------------------------------------------------------#
class FirefoxTest(LearningTest):
    """Run LearningTest using Firefox."""

    drivername = "firefox"

    def setUp(self):
        """Return logged in drivers for Chrome and Firefox."""
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = True
        self.driver = self.login(webdriver.Firefox(profile))


if __name__ == "__main__":
    unittest.main()
