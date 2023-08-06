# STAF (SpeedBoat Test Automation Framework)

## Features

1. Multiple Browser Support
   - Chrome (As of now)
   - Other browser support is **In Progress**
2. Support for mostly all known platforms***
3. Support for Page Object Patterns 
4. Loaded with SeleniumWebdriver Wrapper library
5. Loaded with Standard TestBase class 
6. Loaded with Standart Test Setup & Tear Down methods
6. Test Parallelization 
7. Test Parameterization 
8. Support for screenshot capture 
9. Support for capturing test steps in reports 
10. Next Generation Test Reports 
11. Support for cool tweaks in the standard reports 
12. Command line Support to trigger tests 
13. Easy Setup 
14. Well Defined Directory Structure 
15. Support for distributing tests accross multiple remote machines **In Progress**


## Key Files
1. `installer.py`
2. `speedboat.py` 
3. requirements.txt 
4. `conftest.py`

## Usage

1. Install STAF (Speedboat Test Automation Framework)
   - `python3 installer.py`
2. Run tests 
   - `python3 speedboat.py -a google -l http://google.com -u panchdev -p Passw0rd -n 4 -r 0 -t allure`

## Tools & Libraries

- Next Generation **Test Automation Framework** for **Python**
  1. [pytest](https://docs.pytest.org/en/7.2.x/contents.html)
  - pytest plugins
    1. pytest plugin that provides access to test session metadata
      - [pytest-metadata](https://pypi.org/project/pytest-metadata/)
    2. The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution.
       - [pytest-xdist](https://pypi.org/project/pytest-xdist/)
    3. Run tests in isolated forked subprocesses
       - [pytest-forked](https://pypi.org/project/pytest-forked/)
    4. pytest plugin to re-run tests to eliminate flaky failures
       - [pytest-rerunfailures](https://pypi.org/project/pytest-rerunfailures/)
    5. Virtual Python Environment builder
       - [virtualenv](https://pypi.org/project/virtualenv/)
    6. YAML parser and emitter for Python
       - [PyYAML](https://pypi.org/project/PyYAML/)
    7. library with cross-python path, ini-parsing, io, code, log facilities
       - [py](https://pypi.org/project/py/)
- **Browser Automation Tool** (Open Source)
  - [Selenium Webdriver 4](https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/)
- **Auto Webdriver Manager**
  - [Webdriver Manager](https://pypi.org/project/webdriver-manager/)
- Next Generation **Test Report Framework**
  - [Allure Framework](https://docs.qameta.io/allure/)
- Simple HTML Test Report Plugin 
  - [pytest-html](https://pypi.org/project/pytest-html/)
- Python build tools
  - [Python Build: build](https://pypi.org/project/build/)
  - [Python Uploader: Twine](https://twine.readthedocs.io/en/stable/#entering-credentials)