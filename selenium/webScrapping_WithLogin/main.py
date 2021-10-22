#!/usr/bin/python3
#########################################MODULES###############################################
import time
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#*******************Starter*********************

url = ""# url that we wanna webscrap
username = #username
password = #password
timeOut = 20
start = float(str(round(time.time() * 1000)))
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--start-maximized")

#**********************************************

#---------------------------------------------------------------------------------------------

browser = webdriver.Chrome(ChromeDriverManager().install()) #intiate a browser driver
browser.set_window_size(1024, 600) #  sets the size of the window
browser.minimize_window() # minimizes the tab , so it doesn't appear on the screen each time

# enable browser logging
browser.get(url)

try:
    #sending username and pass section
    userElem = browser.find_element_by_id('username')#find element by id (can be any other thing) 
    userElem.send_keys(username)#perform the action
    userPass = browser.find_element_by_id('password')
    userPass.send_keys(password)
    browser.find_element_by_id("Login").click()#click the specificied element
    #----------------------------------
    #---------------------

    time.sleep(2)#wait 2 sec

    #Read and Execute the script.
    with open('SFsorter.js', 'r') as jquery_js:
        # 3) Read the jquery from a file
        jquery = jquery_js.read()#read the script

    browser.execute_script(jquery)#execute

    #-----------------------------------------


    time.sleep(1200)#wait till the browser disappears

    #------------------------------------------------

except WebDriverException as e:# if there is a problem
    print('CRITICAL: Failed to open {0}'.format(url), e.__class__.__name__)
    browser.quit()
    exit(2)
    
############## END ############### END ############ END ############### END ############# END #################    
