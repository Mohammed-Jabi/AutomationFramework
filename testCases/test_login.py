from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.login_page import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self, setup: WebDriver):

        self.logger.info("********** Test 001 **********")
        self.logger.info("********** Verifying the title of Login Page **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("********** Home page title is passed **********")
            assert True
        else:
            self.driver.save_screenshot("/home/jabir/Automation/Framework/Screenshorts/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("********** Home page title is failed **********")
            assert False



    def test_login(self, setup: WebDriver):
        self.logger.info("********** Verifying the login test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("********** Login page title is passed **********")
            assert True
        else:
            self.driver.save_screenshot("/home/jabir/Automation/Framework/Screenshorts/" + "test_login.png")
            self.driver.close()
            self.logger.info("********** Login page title is passed **********")
            assert False

    
