[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=UNHBAGR6LARES&no_recurring=0&currency_code=AUD)
[![Donate](https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-yellow)](https://www.buymeacoffee.com/ExperimentalNet)


# Pda-Auto-Booker
This is an application that I have built to get tests on the [Practical Driving Assessment Bookings Site](https://online.transport.wa.gov.au/pdabooking/manage/?1) for Western Australia. With this you wont need to check back every hour to see if there is a test available

# Install
Head over to the [release tab](https://github.com/The-Drobe/pda-auto-booker/releases/) and download the zip. This application only supports windows at the moment. <br>
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

# Notes
Currently prints out the following error message this message is fine just ignore it the script is still running
![errorthatisfine.PNG](https://github.com/The-Drobe/pda-auto-booker/blob/main/ReadmeFiles/img/errorthatisfine.PNG?raw=true)

Bitdefender flags the release files as malicious this is a false positive you can review the code if you dont belive me. The code is complied to an exe via [pyinstaller](https://pyinstaller.org/en/stable/). VirusTotal link [here](https://www.virustotal.com/gui/file/98954bca7bb1ffa807fbd280f1d667d1309bdb3aacd893e78f93a6216a5b588d/detection).