from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
import os
class main():
    # options = Options()
    # options.add_argument("--headless")
    # options.binary_location = "chromium/chrome.exe"
    # driver = webdriver.Chrome(service=Service("chromedriver.exe"), chrome_options=options)
    def imports(self):
        with open("userdata.txt", "r") as file:
            # LicenceNumber;Expirydate;FirstName;Surname;DateOfBirth
            userdata = file.read()
        self.userdata = userdata.split(";")
        self.LicenceNumber = self.userdata[0]
        self.Expirydate = self.userdata[1]
        self.FirstName = self.userdata[2]
        self.Surname = self.userdata[3]
        self.DateOfBirth = self.userdata[4]

        with open("DateRangeTimeRange.txt", "r") as file:
            # LicenceNumber;Expirydate;FirstName;Surname;DateOfBirth
            DateRangeTimeRange = file.read()
        self.DateRangeTimeRange = DateRangeTimeRange.split(";")
        self.MinDate = self.DateRangeTimeRange[0]
        self.MaxDate = self.DateRangeTimeRange[1]
        self.MinTime = self.DateRangeTimeRange[2]
        self.MaxTime = self.DateRangeTimeRange[3]

        # print(userdata)

        with open("SitesToBookMetro.txt", "r") as file:
            SitesToBookMetro = file.read()
        self.SitesToBookMetro = SitesToBookMetro.split(";")
        with open("SitesToBookRegional.txt", "r") as file:
            SitesToBookRegional = file.read()
        self.SitesToBookRegional = SitesToBookRegional.replace("\n", "")
        self.SitesToBookRegional = self.SitesToBookRegional.split(";")

        # print(SitesToBookRegional)

    def login(self):
        self.driver.get("https://online.transport.wa.gov.au/pdabooking/manage/?0")
        self.driver.find_element(by=By.NAME, value="clientDetailsPanel:licenceNumber").send_keys(self.LicenceNumber)
        self.driver.find_element(by=By.NAME, value="clientDetailsPanel:licenceExpiryDate").send_keys(self.Expirydate)
        self.driver.find_element(by=By.NAME, value="clientDetailsPanel:firstName").send_keys(self.FirstName)
        self.driver.find_element(by=By.NAME, value="clientDetailsPanel:lastName").send_keys(self.Surname)
        self.driver.find_element(by=By.NAME, value="clientDetailsPanel:dateOfBirth").send_keys(self.DateOfBirth)
        self.driver.find_element(by=By.ID, value="id5").click()
        sleep(3)
        self.driver.find_element(by=By.ID, value="id12").click()
        sleep(3)

    def FindTest(self):
        self.driver.find_element(by=By.ID, value="id16-METRO").click()
        sleep(1)
        for sites in self.SitesToBookMetro:
            self.driver.implicitly_wait(5)
            site = Select(self.driver.find_element(by=By.ID, value="id1c"))
            try:
                site.select_by_visible_text(sites)
            except Exception as e:
                ThePointOfLife = e
            self.driver.find_element(by=By.ID, value="id1d").click()
            if self.driver.find_elements(by=By.XPATH, value='//*[@id="id1e"]/span'):
                # print(True)
                count = -1
                for i in self.driver.find_elements(By.ID, "searchResultRadioLabel"):
                    count = count + 1
                    TimeDate = i.text.replace(" ", "")
                    TimeDate = TimeDate.split("at")
                    # print(TimeDate[0], TimeDate[1])
                    # make 24 hour:
                    Time12 = TimeDate[1]
                    if "PM" in Time12:
                        Time12 = Time12.replace("PM", "")
                        Time12 = Time12.split(":")
                        if Time12[0] != "12":
                            Time12[0] = int(Time12[0]) + 12
                        Time12 = str(Time12[0]) + ":" + Time12[1]
                    else:
                        Time12 = Time12.replace("AM", "")
                    Time = Time12
                    # print(Time)
                    # check date
                    TestdateCheck = datetime.datetime.strptime(TimeDate[0], "%d/%m/%Y")
                    startdate = datetime.datetime.strptime(self.MinDate, "%d/%m/%Y")
                    enddate = datetime.datetime.strptime(self.MaxDate, "%d/%m/%Y")

                    MinTimeIn = str(self.MinTime).split(':')
                    MaxTimeIn = str(self.MaxTime).split(":")
                    TimeIn = Time.split(":")
                    starttime = datetime.time(int(MinTimeIn[0]), int(MinTimeIn[1]), 0)
                    endtime = datetime.time(int(MaxTimeIn[0]), int(MaxTimeIn[1]), 0)
                    TestTime = datetime.time(int(TimeIn[0]), int(TimeIn[1]), 0)

                    if startdate <= TestdateCheck <= enddate and starttime <= TestTime <= endtime:
                        # book test
                        # print("testbooked")
                        searchResultRadioid = "searchResultRadio" + str(count)
                        self.driver.find_element(by=By.ID, value=searchResultRadioid).click()
                        # print(sites, TimeDate)
                        self.driver.find_element(by=By.ID, value="id24").click()
                        self.driver.implicitly_wait(2)
                        return

        # for Regional
        self.driver.find_element(by=By.ID, value="id16-REGIONAL").click()
        sleep(1)
        for sites in self.SitesToBookRegional:
            self.driver.implicitly_wait(5)
            site = Select(self.driver.find_element(by=By.ID, value="id1c"))
            try:
                site.select_by_visible_text(sites)
            except Exception as e:
                ThePointOfLife = e
            self.driver.find_element(by=By.ID, value="id1d").click()
            if self.driver.find_elements(by=By.XPATH, value='//*[@id="id1e"]/span'):
                # print(True)
                count = -1
                for i in self.driver.find_elements(By.ID, "searchResultRadioLabel"):
                    count = count + 1
                    TimeDate = i.text.replace(" ", "")
                    TimeDate = TimeDate.split("at")
                    # print(TimeDate[0], TimeDate[1])
                    # make 24 hour:
                    Time12 = TimeDate[1]
                    if "PM" in Time12:
                        Time12 = Time12.replace("PM", "")
                        Time12 = Time12.split(":")
                        if Time12[0] != "12":
                            Time12[0] = int(Time12[0]) + 12
                        Time12 = str(Time12[0]) + ":" + Time12[1]
                    else:
                        Time12 = Time12.replace("AM", "")
                    Time = Time12
                    # print(Time)
                    # check date
                    TestdateCheck = datetime.datetime.strptime(TimeDate[0], "%d/%m/%Y")
                    startdate = datetime.datetime.strptime(self.MinDate, "%d/%m/%Y")
                    enddate = datetime.datetime.strptime(self.MaxDate, "%d/%m/%Y")

                    MinTimeIn = str(self.MinTime).split(':')
                    MaxTimeIn = str(self.MaxTime).split(":")
                    TimeIn = Time.split(":")
                    starttime = datetime.time(int(MinTimeIn[0]), int(MinTimeIn[1]), 0)
                    endtime = datetime.time(int(MaxTimeIn[0]), int(MaxTimeIn[1]), 0)
                    TestTime = datetime.time(int(TimeIn[0]), int(TimeIn[1]), 0)

                    if startdate <= TestdateCheck <= enddate and starttime <= TestTime <= endtime:
                        # book test
                        # print("testbooked")
                        searchResultRadioid = "searchResultRadio" + str(count)
                        self.driver.find_element(by=By.ID, value=searchResultRadioid).click()
                        # print(sites, TimeDate)
                        self.driver.find_element(by=By.ID, value="id24").click()
                        self.driver.implicitly_wait(2)
                        return(sites, TimeDate)

            self.driver.implicitly_wait(2)
            self.FindTest()

    def start(self, head):
        self.imports()
        self.options = Options()
        if not head:
            self.options.add_argument("--headless")
        self.options.binary_location = "chromium/chrome.exe"
        self.driver = webdriver.Chrome(service=Service("chromedriver.exe"), chrome_options=self.options)
        self.login()
        out = self.FindTest()
        os.system('cls')
        print('''                                                                                 
        _____ ____  _____    _____ _____ _____ _____    _____ _____ _____ _____ _____ _____ 
        |  _  |    \|  _  |  |  _  |  |  |_   _|     |  | __  |     |     |  |  |   __| __  |
        |   __|  |  |     |  |     |  |  | | | |  |  |  | __ -|  |  |  |  |    -|   __|    -|
        |__|  |____/|__|__|  |__|__|_____| |_| |_____|  |_____|_____|_____|__|__|_____|__|__|                                                                                    
        ''')
        print('''
    _______ ______  _____ _______   ______ ____  _    _ _   _ _____  
    |__   __|  ____|/ ____|__   __| |  ____/ __ \| |  | | \ | |  __ \ 
        | |  | |__  | (___    | |    | |__ | |  | | |  | |  \| | |  | |
        | |  |  __|  \___ \   | |    |  __|| |  | | |  | | . ` | |  | |
        | |  | |____ ____) |  | |    | |   | |__| | |__| | |\  | |__| |
        |_|  |______|_____/   |_|    |_|    \____/ \____/|_| \_|_____/                                                                 
        ''')
        print(out)
        input("press any key to exit: ")


    # if __name__ == '__main__':
    #     login()
    #     print("Test found: " + str(FindTest()))
    #     input("press any key to exit: ")

    # Copyright 2022 Giles Wardrobe