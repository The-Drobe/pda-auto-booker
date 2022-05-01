import os
import inquirer
from time import sleep

def MainMenu():
    os.system('cls')
    print('''                                                                                 
     _____ ____  _____    _____ _____ _____ _____    _____ _____ _____ _____ _____ _____ 
    |  _  |    \|  _  |  |  _  |  |  |_   _|     |  | __  |     |     |  |  |   __| __  |
    |   __|  |  |     |  |     |  |  | | | |  |  |  | __ -|  |  |  |  |    -|   __|    -|
    |__|  |____/|__|__|  |__|__|_____| |_| |_____|  |_____|_____|_____|__|__|_____|__|__|                                                                                    
    ''')

    print("1) Setup")
    print("2) Start")
    print("3) Set Time Range")
    print("4) Select Sites")
    
    UserSelection = input("Selection: ")

    if UserSelection == "1":
        SetUp()
    elif UserSelection == "2":
        import bot
        bot.start()
    elif UserSelection == "3":
        TimeRange()
    elif UserSelection == "4":
        SelectSites()
    else:
        MainMenu()

def SetUp():
    os.system('cls')
    print('''                                                                                 
     _____ ____  _____    _____ _____ _____ _____    _____ _____ _____ _____ _____ _____ 
    |  _  |    \|  _  |  |  _  |  |  |_   _|     |  | __  |     |     |  |  |   __| __  |
    |   __|  |  |     |  |     |  |  | | | |  |  |  | __ -|  |  |  |  |    -|   __|    -|
    |__|  |____/|__|__|  |__|__|_____| |_| |_____|  |_____|_____|_____|__|__|_____|__|__|                                                                                    
    ''')
    LicenceNumber = input("Please input LicenceNumber: ")
    Expirydate = input("Please input Expirydate of Licence in d/m/y: ")
    FirstName = input("Please input First Name: ")
    Surname = input("Please input Last Name: ")
    DateOfBirth = input("Please input DateOfBirth in d/m/y: ")
    fileoutput = LicenceNumber + ";" + Expirydate + ";" + FirstName + ";" + Surname + ";" + DateOfBirth

    # write to file:
    with open("userdata.txt", "w") as file:
        file.write(fileoutput)

    # select
    # metro
    # use this readchar to get it working on windows https://github.com/Cube707/python-readchar this is the pull request https://github.com/magmax/python-readchar/pull/71
    with open("data/SitesToBookMetro.txt.orig", "r") as file:
        SitesToBookMetro = file.read()
    SitesToBookMetro = SitesToBookMetro.split(";")
    os.system('cls')
    questions = [
        inquirer.Checkbox('SitesToBookMetro',
                          message="Please Select The Metro Sites that you want (leave blank for none)",
                          choices=SitesToBookMetro,
                          carousel=True,
                          ),
    ]
    SitesToBookMetroOut = inquirer.prompt(questions)

    # Regional
    with open("data/SitesToBookRegional.txt.orig", "r") as file:
        SitesToBookRegional = file.read()
    SitesToBookRegional = SitesToBookRegional.replace("\n", "")
    SitesToBookRegional = SitesToBookRegional.split(";")
    os.system('cls')
    questions = [
        inquirer.Checkbox('SitesToBookRegional',
                          message="Please Select The Regional Sites that you want (leave blank for none)",
                          choices=SitesToBookRegional,
                          carousel=True,
                          ),
    ]
    SitesToBookRegionalOut = inquirer.prompt(questions)

    # put metro into file:
    for key, value in SitesToBookMetroOut.items():
        SitesToBookMetroOut = value

    SitesToBookMetroWrite = ""
    for i in SitesToBookMetroOut:
        SitesToBookMetroWrite = SitesToBookMetroWrite + ";" + i

    SitesToBookMetroWrite = SitesToBookMetroWrite[1:]

    with open("SitesToBookMetro.txt", "w") as file:
        file.write(SitesToBookMetroWrite)

    # put Regional into file:
    for key, value in SitesToBookRegionalOut.items():
        SitesToBookRegionalOut = value

    SitesToBookRegionalWrite = ""
    for i in SitesToBookRegionalOut:
        SitesToBookRegionalWrite = SitesToBookRegionalWrite + ";" + i

    SitesToBookRegionalWrite = SitesToBookRegionalWrite[1:]

    with open("SitesToBookRegional.txt", "w") as file:
        file.write(SitesToBookRegionalWrite)

    # DateRange
    MinDate = input("Please input earliest date d/m/y: ")
    MaxDate = input("Please input latest date d/m/y: ")
    MinTime = input("Please input earliest time in 24 hour time e.g. 17:00 : ")
    MaxTime = input("Please input latest time in 24 hour time e.g. 17:00 : ")
    TimeRangeOut = MinDate + ";" + MaxDate + ";" + MinTime + ";" + MaxTime

    with open("DateRangeTimeRange.txt", "w") as file:
        file.write(TimeRangeOut)

    print("Setup complete start bot on the main menu")
    sleep(2)
    MainMenu()


def SelectSites():
    # metro
    # use this readchar to get it working on windows https://github.com/Cube707/python-readchar this is the pull request https://github.com/magmax/python-readchar/pull/71
    with open("data/SitesToBookMetro.txt.orig", "r") as file:
        SitesToBookMetro = file.read()
    SitesToBookMetro = SitesToBookMetro.split(";")
    os.system('cls')
    questions = [
        inquirer.Checkbox('SitesToBookMetro',
                          message="Please Select The Metro Sites that you want (leave blank for none)",
                          choices=SitesToBookMetro,
                          carousel=True,
                          ),
    ]
    SitesToBookMetroOut = inquirer.prompt(questions)

    # Regional
    with open("data/SitesToBookRegional.txt.orig", "r") as file:
        SitesToBookRegional = file.read()
    SitesToBookRegional = SitesToBookRegional.replace("\n", "")
    SitesToBookRegional = SitesToBookRegional.split(";")
    os.system('cls')
    questions = [
        inquirer.Checkbox('SitesToBookRegional',
                          message="Please Select The Regional Sites that you want (leave blank for none)",
                          choices=SitesToBookRegional,
                          carousel=True,
                          ),
    ]
    SitesToBookRegionalOut = inquirer.prompt(questions)

    # put metro into file:
    for key, value in SitesToBookMetroOut.items():
        SitesToBookMetroOut = value

    SitesToBookMetroWrite = ""
    for i in SitesToBookMetroOut:
        SitesToBookMetroWrite = SitesToBookMetroWrite + ";" + i

    SitesToBookMetroWrite = SitesToBookMetroWrite[1:]

    with open("SitesToBookMetro.txt", "w") as file:
        file.write(SitesToBookMetroWrite)

    # put Regional into file:
    for key, value in SitesToBookRegionalOut.items():
        SitesToBookRegionalOut = value

    SitesToBookRegionalWrite = ""
    for i in SitesToBookRegionalOut:
        SitesToBookRegionalWrite = SitesToBookRegionalWrite + ";" + i

    SitesToBookRegionalWrite = SitesToBookRegionalWrite[1:]

    with open("SitesToBookRegional.txt", "w") as file:
        file.write(SitesToBookRegionalWrite)

    MainMenu()

def TimeRange():
    MinDate = input("Please input earliest date d/m/y: ")
    MaxDate = input("Please input latest date d/m/y: ")
    MinTime = input("Please input earliest time in 24 hour time e.g. 17:00 : ")
    MaxTime = input("Please input latest time in 24 hour time e.g. 17:00 : ")
    TimeRangeOut = MinDate + ";" + MaxDate + ";" + MinTime + ";" + MaxTime

    with open("DateRangeTimeRange.txt", "w") as file:
        file.write(TimeRangeOut)


if __name__ == "__main__":
    MainMenu()

# Copyright 2022 Giles Wardrobe