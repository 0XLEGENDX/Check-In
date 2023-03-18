import json
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import random

from fake_useragent import UserAgent
import time


def performRead():
  pass


def performWrite():
  pass

def getRandTime():

  return random.randint(3,9)


# opening files to retrive all the stored data

fileHandler = open('accounts.txt', 'r')
accountsHandler = open('accountsJson.txt', 'r')

# If the files are empty then this will create demo data

if (fileHandler.read() == ""):

  print("File Empty Adding Demo Data")

  demoAccountsJson = json.dumps({
    '7219279796': 'anurag',
    '9404347906': 'Yoyoaniket2'
  })
  demoAccounts = "9404347906"
  fileHandler = open('accounts.txt', 'w')
  accountsHandler = open('accountsJson.txt', 'w')

  fileHandler.write(demoAccounts)
  accountsHandler.write(demoAccountsJson)

fileHandler = open('accounts.txt', 'r')
accountsHandler = open('accountsJson.txt', 'r')

# Loads the list of accounts and passwords
passwordDictionary = json.loads(accountsHandler.read())
listOfAccounts = (fileHandler.read()).split()

print("The total list of accounts and password is : ")
print(passwordDictionary)
print(listOfAccounts)

addedNewAccountInterrupt = False
listOfNewAccountsAdded = {}

localDataHandler = open('lastDate.txt', 'r')
currentId = 0

while (True):

  if (addedNewAccountInterrupt):
    pass
  else:

    if (str(date.today) != localDataHandler.read().strip()):

      localDataHandler = open('lastDate.txt', 'w')
      localDataHandler.write(str(date.today()))
      print(date.today())
      localDataHandler = open('lastDate.txt', 'r')

      options = Options()
      options.add_argument('--no-sandbox')
      options.add_argument('--disable-dev-shm-usage')
      options.add_argument("start-maximized")
      #options.add_argument('headless')
      options.add_experimental_option("excludeSwitches", ["enable-automation"])
      options.add_experimental_option('useAutomationExtension', False)

      driver = webdriver.Chrome(options=options)

      
      #driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"""})
      driver.get('https://www.fiewin.com/#/Login')
      # driver.execute_script(
      #   "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
      # )

      time.sleep(10)

      #driver.find_element_by_id("Password Login").click()  css-901oao r-b88u0q
      count = 0
      

    # Get all the elements available with tag name 'p'
      elements = driver.find_elements(By.TAG_NAME, 'div')
      elements[12].click()
      # for e in elements:
      #   if(count==12):
      #     try:
      #       e.click()
      #     except:
      #       pass
      #   count+=1


      #Select and enter number in login
      elements = driver.find_elements(By.TAG_NAME, 'input')
      elements[0].send_keys(listOfAccounts[currentId])
      time.sleep(getRandTime())

      #Select and enter password in login
      elements = driver.find_elements(By.TAG_NAME, 'input')
      elements[1].send_keys(passwordDictionary[listOfAccounts[currentId]])
      time.sleep(getRandTime())

      #Login using creds
      elements = driver.find_elements(By.TAG_NAME, 'div')
      elements[25].click()
      time.sleep(getRandTime())

      #CLosing the banners
      elements = driver.find_elements(By.TAG_NAME, 'img')
      try:
        elements[16].click()
      except:
        try:
          elements[15].click()
        except:
          pass

      #Checking the balance for errors

      # balance = 0
      # count = 0

      # elements = driver.find_elements(By.TAG_NAME, 'div')
      # try:
      #   balance = int((elements[16].text))
      # except:
      #   balance = int(((elements[18].text).replace("rupee","")))
      
      # print(balance)

      # for element in elements:
      #   try:
      #     print(element.text)
      #     print(count)
      #   except:
      #     print("Ran into error")
      #   count+=1
      

      time.sleep(getRandTime())

      driver.get("https://www.fiewin.com/#/CheckIn")
      
      time.sleep(getRandTime())

      elements = driver.find_elements(By.TAG_NAME, 'div')
      try:
        elements[54].click()
        try:
          elements[55].click()
        except:
          pass
      except:
        try:
          elements[55].click()
        except:
          pass

      
      print("Done checkin for : " + listOfAccounts[currentId])
      currentId+=1
      
      driver.quit()

      

      if(currentId>=len(listOfAccounts)):
        time.sleep(86400)
        print("Completed Todays Work Sleeping Now")
        currentId = 0
      time.sleep(10)

