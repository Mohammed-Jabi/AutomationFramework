from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    return driver
   

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##Generating pyTest HTML reports
def pytest_configure(config):
    config.addinivalue_line('markers', 'ProjectName: nop Commerce')
    config.addinivalue_line('markers', 'ModuleName: Customers')
    config.addinivalue_line('markers', 'Tester: Mohammed Jabir')

@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'nop Commerce'
    metadata['Module Name'] = 'Customers'
    metadata['Tester'] = 'Mohammed Jabir'


