import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from config import config, paths
from helpers import common


class DriverManager:

    @staticmethod
    def get_browser(browser: str):

        if browser == config.BROWSER_CHROME:
            if browser == config.BROWSER_CHROME:
                # create an instance of Chrome webdriver
                # return webdriver.Chrome(DriverManager.get_driver_file_path(browser))

                # Doc: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
                # GitHub: https://github.com/SergeyPirogov/webdriver_manager
                # GitHub: https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/test_install_drivers.py#L15-L17
                service = ChromeService(executable_path=ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service)
                return driver

        elif browser == config.BROWSER_HEADLESS_CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--headless')
            chrome_driver_path = DriverManager.get_driver_file_path(browser)
            return webdriver.Chrome(executable_path = chrome_driver_path,options=chrome_options)


    @staticmethod
    def get_driver_file_path(browser: str):
        sep = os.sep
        if browser == config.BROWSER_CHROME\
                or browser == config.BROWSER_HEADLESS_CHROME:

            # prepare driver_file_name
            driver_file_name = config.OS_DARWIN + sep + config.DRIVER_NAME_CHROME \
                if common.get_os() == config.OS_DARWIN \
                else config.OS_LINUX_KERNER_BASED + sep + config.DRIVER_NAME_CHROME \
                if config.OS_LINUX_KERNER_BASED in common.get_os() else config.OS_WINDOWS + sep + config.DRIVER_NAME_CHROME + config.EXTENTION_WINDOWS

            # Print
            print(paths.DRIVERS_DIR_WITH_SLASH + driver_file_name)
            # return chrome driver path
            return paths.DRIVERS_DIR_WITH_SLASH + driver_file_name