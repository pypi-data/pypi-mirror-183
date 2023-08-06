import asyncio
import json
import os
import platform
import re
import time

import chromedriver_autoinstaller
import markdownify
import undetected_chromedriver as uc
import urllib3
from pyvirtualdisplay import Display
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
urllib3.disable_warnings()

def run(driver, search):
    try:
        URL = f"https://you.com/search?q={search}&tbm=youcode"
    
        driver.get(URL)
        delay = 3 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-e6327d8-2 gaUktj')))
        except TimeoutException:
            pass
            
        
        html = driver.execute_script('return document.documentElement.outerHTML')
        soup = BeautifulSoup(html, 'lxml')
        data = [item['data-eventactioncontent'] for item in soup.find_all() if 'data-eventactioncontent' in item.attrs]
    except:
        data = []
        
    
    # Empty list to store the output
    return data


class Code:
    """
    An unofficial Python wrapper for YOU.com YOUCHAT
    """

    # def __init__(
    #     self,
    #     verbose: bool = False,
    #     window_size: tuple = (800, 600),
    #     driver: object = None,
    # ) -> None:

    #     self.__verbose = verbose
    #     self.__driver = driver

    def find_code(driver, search: str) -> dict:

        """
        Send a message to YouChat\n
        Parameters:
        - message: The message you want to send\n
        - driver: pass the driver form the Init variable\n
        Returns a `dict` with the following keys:
        - message: The response from YouChat\n
        - time: the time it took to complete your request
        """
        start = time.time()
        

        index = 1
        data = run(driver, search)
        runs = 0
        while True:
            if runs == 6:
                data = []
                break
            if not data:
                runs += 1
                data = run(driver, search)
            if data:
                break



        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        if runs == 0:
            runs = 1
        
        return {"response": data, "time": str(timedate), "runs": str(runs)}
