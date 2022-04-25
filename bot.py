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

options = Options()
options.add_argument("--headless")
options.binary_location = "chromium/chrome.exe"
driver = webdriver.Chrome(service=Service("chromedriver.exe"), chrome_options=options)

with open("userdata.txt", "r") as file:
    # LicenceNumber;Expirydate;FirstName;Surname;DateOfBirth
    userdata = file.read()
userdata = userdata.split(";")
LicenceNumber = userdata[0]
Expirydate = userdata[1]
FirstName = userdata[2]
Surname = userdata[3]
DateOfBirth = userdata[4]

with open("DateRangeTimeRange.txt", "r") as file:
    # LicenceNumber;Expirydate;FirstName;Surname;DateOfBirth
    DateRangeTimeRange = file.read()
DateRangeTimeRange = DateRangeTimeRange.split(";")
MinDate = DateRangeTimeRange[0]
MaxDate = DateRangeTimeRange[1]
MinTime = DateRangeTimeRange[2]
MaxTime = DateRangeTimeRange[3]

# print(userdata)

with open("SitesToBookMetro.txt", "r") as file:
    SitesToBookMetro = file.read()
SitesToBookMetro = SitesToBookMetro.split(";")
with open("SitesToBookRegional.txt", "r") as file:
    SitesToBookRegional = file.read()
SitesToBookRegional = SitesToBookRegional.replace("\n", "")
SitesToBookRegional = SitesToBookRegional.split(";")

# print(SitesToBookRegional)

def login():
    driver.get("https://online.transport.wa.gov.au/pdabooking/manage/?0")
    driver.find_element(by=By.NAME, value="clientDetailsPanel:licenceNumber").send_keys(LicenceNumber)
    driver.find_element(by=By.NAME, value="clientDetailsPanel:licenceExpiryDate").send_keys(Expirydate)
    driver.find_element(by=By.NAME, value="clientDetailsPanel:firstName").send_keys(FirstName)
    driver.find_element(by=By.NAME, value="clientDetailsPanel:lastName").send_keys(Surname)
    driver.find_element(by=By.NAME, value="clientDetailsPanel:dateOfBirth").send_keys(DateOfBirth)
    driver.find_element(by=By.ID, value="id5").click()
    sleep(3)
    driver.find_element(by=By.ID, value="id12").click()
    sleep(3)

def FindTest():
    driver.find_element(by=By.ID, value="id16-METRO").click()
    sleep(1)
    for sites in SitesToBookMetro:
        driver.implicitly_wait(5)
        site = Select(driver.find_element(by=By.ID, value="id1c"))
        try:
            site.select_by_visible_text(sites)
        except Exception as e:
            ThePointOfLife = e
        driver.find_element(by=By.ID, value="id1d").click()
        if driver.find_elements(by=By.XPATH, value='//*[@id="id1e"]/span'):
            # print(True)
            count = -1
            for i in driver.find_elements(By.ID, "searchResultRadioLabel"):
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
                startdate = datetime.datetime.strptime(MinDate, "%d/%m/%Y")
                enddate = datetime.datetime.strptime(MaxDate, "%d/%m/%Y")

                MinTimeIn = str(MinTime).split(':')
                MaxTimeIn = str(MaxTime).split(":")
                TimeIn = Time.split(":")
                starttime = datetime.time(int(MinTimeIn[0]), int(MinTimeIn[1]), 0)
                endtime = datetime.time(int(MaxTimeIn[0]), int(MaxTimeIn[1]), 0)
                TestTime = datetime.time(int(TimeIn[0]), int(TimeIn[1]), 0)

                if startdate <= TestdateCheck <= enddate and starttime <= TestTime <= endtime:
                    # book test
                    # print("testbooked")
                    searchResultRadioid = "searchResultRadio" + str(count)
                    driver.find_element(by=By.ID, value=searchResultRadioid).click()
                    # print(sites, TimeDate)
                    driver.find_element(by=By.ID, value="id24").click()
                    driver.implicitly_wait(2)
                    return

    # for Regional
    driver.find_element(by=By.ID, value="id16-REGIONAL").click()
    sleep(1)
    for sites in SitesToBookRegional:
        driver.implicitly_wait(5)
        site = Select(driver.find_element(by=By.ID, value="id1c"))
        try:
            site.select_by_visible_text(sites)
        except Exception as e:
            ThePointOfLife = e
        driver.find_element(by=By.ID, value="id1d").click()
        if driver.find_elements(by=By.XPATH, value='//*[@id="id1e"]/span'):
            # print(True)
            count = -1
            for i in driver.find_elements(By.ID, "searchResultRadioLabel"):
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
                startdate = datetime.datetime.strptime(MinDate, "%d/%m/%Y")
                enddate = datetime.datetime.strptime(MaxDate, "%d/%m/%Y")

                MinTimeIn = str(MinTime).split(':')
                MaxTimeIn = str(MaxTime).split(":")
                TimeIn = Time.split(":")
                starttime = datetime.time(int(MinTimeIn[0]), int(MinTimeIn[1]), 0)
                endtime = datetime.time(int(MaxTimeIn[0]), int(MaxTimeIn[1]), 0)
                TestTime = datetime.time(int(TimeIn[0]), int(TimeIn[1]), 0)

                if startdate <= TestdateCheck <= enddate and starttime <= TestTime <= endtime:
                    # book test
                    # print("testbooked")
                    searchResultRadioid = "searchResultRadio" + str(count)
                    driver.find_element(by=By.ID, value=searchResultRadioid).click()
                    # print(sites, TimeDate)
                    driver.find_element(by=By.ID, value="id24").click()
                    driver.implicitly_wait(2)
                    return(sites, TimeDate)

        driver.implicitly_wait(2)
        FindTest()

def start():
    login()
    out = FindTest()
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
