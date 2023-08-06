import pytest

from helpers.Page import Page


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('password')
@pytest.mark.usefixtures('username')
@pytest.mark.usefixtures('url')
class TestPyTest:

    @pytest.mark.skip
    def test_passing(self, url, username, password):

        print("{0}, {1}, {2}", url, username, password)

        pageGoogleHome = Page(self.driver)

        print("appple")
        pageGoogleHome.log.info("Open Apple.com")
        pageGoogleHome.get("http://apple.com")

        assert 1 == 1

    @pytest.mark.skip
    def test_failing(self, url, username, password):

        print("{0}, {1}, {2}", url, username, password)

        pageGoogleHome = Page(self.driver)


        pageGoogleHome.log.info("Open Google.com")
        pageGoogleHome.get("http://google.com")

        assert 1 == 2




