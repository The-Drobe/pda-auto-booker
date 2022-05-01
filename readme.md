[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=UNHBAGR6LARES&no_recurring=0&currency_code=AUD)
[![Donate](https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow)](https://www.buymeacoffee.com/ExperimentalNet)


# Pda-Auto-Booker
This is an application that I have built to get tests on the [Practical Driving Assessment Bookings Site](https://online.transport.wa.gov.au/pdabooking/manage/?1) for Western Australia. With this you wont need to check back every hour to see if there is a test available

# Install
Head over to the release tab and download the zip. This application only supports windows at the moment. <br>
1. Unzip the file
2. run main.exe
3. Select setup with the number 1 and follow the setup through
4. Run the Bot and wait untill it finds a test with what you specified

# Issues
If any issues apppear report them in the issues tab

# To run the Script On Windows
There is a currently a bug in the python-readchar module That prevents the interface from functioning properly on Windows. It has been fixed in this fork https://github.com/Cube707/python-readchar you will need to install this after installing inquirer

Pull request: https://github.com/magmax/python-readchar/pull/71

# Running The script
1. clone this repo
2. run `pip install -r requirements.txt`
3. run main.py with `python main.py` 
