import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:

    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMailGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstitemAdministrators_xpath = "//select[@id='SelectedCustomerRoleIds']/option[text()='Administrators']"
    lstitemRegistered_xpath = "//select[@id='SelectedCustomerRoleIds']/option[text()='Registered')]"
    lstitemGuests_xpath = "//select[@id='SelectedCustomerRoleIds']/option[text()='Guests')]"
    lstitemVendor_xpath = "//select[@id='SelectedCustomerRoleIds']/option[text()='Vendors']"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContebt_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    canclebutton_xpath = "//span[@class='k-icon k-i-close']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomer(self, role):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.canclebutton_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    

    def setManagerVendor(self, value):
        time.sleep(3)
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)
    
    # Example: If you need to interact with another element to confirm the selection
    # Replace the next line with the action that confirms the selection, if needed
    # self.driver.find_element(By.XPATH, "xpath_of_an_element_to_confirm_selection").click()

     

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMailGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
    
    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)
    
    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)
    
    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContentent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContebt_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
    