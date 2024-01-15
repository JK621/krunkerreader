
import parse
import time
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


lib = parse.parseInputList()    # Take input
length = len(lib)               # Get Length of inserted List
count = length                  # Copy list length to second Variable to be used as seperate count



def sortList(lib, count):
    
    LVL20 = []
    LVL15 = []

    driver = webdriver.Chrome()     # Create Selenium Chrome Instance to be used for profile checking

    for a in lib:                   # Loop going trough every Index of the list

        count -= 1                              # Displays Number of Account in List 
        Details = parse.parseAccountData(a)     # Get Password and Account name to display in Output
        
        driver.get("https://krunker.io/social.html?p=profile&q="+Details[0])    # Open Profile Tab of current selected Account
        time.sleep(1)                                                           # Delay to ensure site loads
        htag = driver.find_element(By.ID, "hackText")                           # Get Hackertag Browser Element
        
        if htag.value_of_css_property("display") == "block":                    # Is the Account Hackertagged
            print("hacker")                                                     # Yes, go to next Account and log
        else:
            try:                                                                # Try Loop to avoid crashing of the Programm if a rare error occurs (for example with deleted Profiles)
                LVL = driver.find_elements(By.CLASS_NAME, "pSt")                            # Get Level Webelement
                print(count, " ", Details, " ", int(parse.parseLevelText(LVL[0].text)))     # Log Details, Level and Count to console
                if int(parse.parseLevelText(LVL[0].text)) > 20:                             # Is the Account LVL20:
                    LVL20.append(Details)                                                   # Yes, add it to the list
                elif int(parse.parseLevelText(LVL[0].text)) > 15:                           # Is the account worth a look?
                    LVL15.append(Details)                                                   # Yes, add it to the list
            except:
                pass                                                                        # No, go the next account
    
    return [LVL20, LVL15]                                                                    # End of Method: return all useable accounts

accounts = sortList(lib, count)

name = ["output", str(random.randint(0,10000)), ".txt"]
filename = "".join(name)                                    # Create name for a new File to save the output to

print("OUTPUT SAVED TO", filename)                          # Log Output file name
f = open(filename, "a")                                     # Create Ouput file

f.write("LVL20+: \n")                                       
for i in accounts[0]:
    f.write(("".join([i[0], " : ", i[1]])))
    f.write("\n")
f.write("\nLVL15-19:")
for i in accounts[1]:
    f.write(("".join([i[0], " : ", i[1]])))
    f.write("\n")
f.close()
