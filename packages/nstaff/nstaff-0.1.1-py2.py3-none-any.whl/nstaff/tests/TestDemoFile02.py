import time

import allure
import pytest

from helpers.Page import Page
from helpers.SpeedBoat import SpeedBoat


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('password')
@pytest.mark.usefixtures('username')
@pytest.mark.usefixtures('url')
class TestDemo(SpeedBoat):

    #@pytest.mark.skip
    @pytest.mark.sanity
    def test_apple_home_page_is_accessible(self, url, username, password):

        print("{0}, {1}, {2}", url, username, password)

        pageGoogleHome = Page(self.driver)

        pageGoogleHome.log.info("Open Apple.com")
        pageGoogleHome.get("http://apple.com")

        assert  1 == 3


    #@pytest.mark.skip
    @pytest.mark.sanity
    def test_google_home_page_is_accessible(self, url, username, password):

        print("{0}, {1}, {2}", url, username, password)

        pageGoogleHome = Page(self.driver)


        pageGoogleHome.log.info("Open Google.com")
        pageGoogleHome.get("http://google.com")



