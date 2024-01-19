import random
import string
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.login_page import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from selenium.webdriver.common.by import By



class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Succesful **********")

        self.logger.info("********** Starting Add Customer Test **********")
        time.sleep(3)
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()
        time.sleep(5)
        self.logger.info("********** Providing customer info **********")
        
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("Test123@")
        print("I am here")
        self.addcust.setCustomer("Vendors")
        print("I am here1")
        time.sleep(3)
        self.addcust.setManagerVendor("Vendor 2")  # Fixed method name
        print("I am here3")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("FirstName")
        self.addcust.setLastName("LastName")
        self.addcust.setDob("10/20/2001")
        self.addcust.setCompanyName("J & H")
        self.addcust.setAdminContentent("This is for testing........")
        self.addcust.clickOnSave()

        self.logger.info("********** Save customer info **********")
        self.logger.info("********** Add customer validation started **********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot("/home/jabir/Automation/Framework/Screenshorts" + "test_addCustomer_src.png")
            self.logger.error("********** Add customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Home Page Title Test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))    
