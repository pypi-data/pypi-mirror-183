import time

import pytest

from helpers.Page import Page
from helpers.SpeedBoat import SpeedBoat


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('password')
@pytest.mark.usefixtures('username')
@pytest.mark.usefixtures('url')
class TestDemo(SpeedBoat):

    @pytest.mark.sanity
    @pytest.mark.skip
    def test_google_home_page_is_accessible(self, url, username, password):

        print("{0}, {1}, {2}", url, username, password)

        pageGoogleHome = Page(self.driver)

        pageGoogleHome.get(url)



