import sys
##########################################################################
############################# GITHUB API #################################
import requests
import os

API_ENDPOINT = "https://api.github.com/repos/nu12/steamdeck/issues"
API_KEY = os.getenv('TOKEN')
data = {
    "title":"Steamdeck may be available",
    "body":"Check steamdeck availability",
    "assignees":["nu12"]
    }

headers = {
    "Accept": "application/vnd.github+json", 
    "Authorization": "Bearer " + API_KEY, 
    "X-GitHub-Api-Version": "2022-11-28"
    }

def create_issue():
    print("Creating issue")
    requests.post(API_ENDPOINT, headers=headers, json=data)
##########################################################################
############################## SELENIUM ##################################
import time 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() 
options.add_argument("--headless") 
options.page_load_strategy = "none"
driver = Chrome(options=options) 
driver.implicitly_wait(5)
url = "https://store.steampowered.com/sale/steamdeckrefurbished/"
driver.get(url) 
time.sleep(5)
##########################################################################
############################## EXECUTION #################################
contents = driver.find_elements(By.CSS_SELECTOR, "div.CartBtn")
for content in contents:
    spans = content.find_elements(By.TAG_NAME, "span")
    for span in spans:
        status = span.get_attribute("textContent")
        print("Status is: " + status)
        # if status == ' Out of stock':
        #     print("Skip")
        #     continue
        if status == ' Épuisé':
            print("Skip")
            continue

        create_issue()
        sys.exit()
##########################################################################
##########################################################################