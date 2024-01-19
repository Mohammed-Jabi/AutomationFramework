from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.login_page import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = "/home/jabir/Automation/Framework/TestData/Login.xlsx"


    logger = LogGen.loggen()


    def test_login(self, setup: WebDriver):
        self.logger.info("********** Test 002 **********")
        self.logger.info("********** Verifying the login DDT test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of rows in the sheet: ", self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1', r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Passed *******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****** Failed *******")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif self.exp != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Failed *******")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("****** Passed *******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test pass")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test fail")
            self.driver.close()
            assert False

        self.logger.info("********** End of Login DDT Test **********")
        self.logger.info("********** Completed_TC_LoginDDT_002 **********")

            













    
