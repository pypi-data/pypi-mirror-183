import asyncio
import json
import os
import platform
import re
import time

import chromedriver_autoinstaller
import markdownify
import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()


class Apps:
    """
    An unofficial Python wrapper for YOU.com YOUCHAT
    """

    def __init__(
        self,
        verbose: bool = False,
        proxy: str = "",
        window_size: tuple = (800, 600),
        : str = "",
    ) -> None:

        self.__verbose = verbose
        self.__proxy = proxy
        
        self._webdriver_path = webdriver_path

        self.__is_headless = platform.system() == "Linux" and "DISPLAY" not in os.environ
        self.__verbose_print("[0] Platform:", platform.system())
        self.__verbose_print("[0] Display:", "DISPLAY" in os.environ)
        self.__verbose_print("[0] Headless:", self.__is_headless)
        


    def __verbose_print(self, *args, **kwargs) -> None:
        """
        Print if verbose is enabled
        """
        if self.__verbose:
            print(*args, **kwargs)


    def get_app(self, name:str, message: str) -> dict:

        """
        Send a message to the chatbot\n
        Parameters:
        - message: The message you want to send\n
        Returns a `dict` with the following keys:
        - message: The message the chatbot sent
        - conversation_id: The conversation ID
        - parent_id: The parent ID
        """
        start = time.time()
        # Ensure that the Cloudflare cookies is still valid
        self.__verbose_print("[send_msg] Ensuring Cloudflare cookies")
        self.driver.get("https://you.com/search?q=" + message)

        # Send the message
        self.__verbose_print("[send_msg] Sending message")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        textbox = self.driver.find_element(By.TAG_NAME, "textarea")

        # Sending emoji (from https://stackoverflow.com/a/61043442)
        textbox.click()
        self.driver.execute_script(
            """
        var element = arguments[0], txt = arguments[1];
        element.value += txt;
        element.dispatchEvent(new Event('change'));
        """,
            textbox,
            message,
        )
        textbox.send_keys(Keys.ENTER)

        # Wait for the response to be ready
        self.__verbose_print("[send_msg] Waiting for completion")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="chatHistory"]/div/div[2]/p/p')))

        # Get the response element
        self.__verbose_print("[send_msg] Finding response element")
        response = self.driver.find_element(By.XPATH, '//*[@id="chatHistory"]/div/div[2]')

        # Check if the response is an error

        # Return the response
        msg = markdownify.markdownify(response.text)

        # type(headers) == str

        # while True:
        #     try:
        #         if WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative"), "New Chat")):
        #             text = self.driver.find_elements(
        #                 By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/nav/div/div/a[1]/div[1]'
        #             )[-1].text
        #             break
        #     except:
        #         continue
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        return {"message": msg, "time": str(timedate)}

    def reset_conversation(self) -> None:
        """
        Reset the conversation
        """
        self.__verbose_print("Resetting conversation")
        self.driver.find_element(By.LINK_TEXT, "New chat").click()
