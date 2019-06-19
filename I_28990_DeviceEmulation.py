import os

from selenium import webdriver
from applitools.selenium.eyes import Eyes
from applitools.selenium.eyes import Target
from applitools.selenium import Region
from applitools.selenium import BatchInfo
from selenium.webdriver.common.by import By

class HelloWorld:

    eyes = Eyes() # eyes-selenium 3.16.2 / selenium 3.141.0
    
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']

    try:
        
        # Open a Chrome browser.
        __mobile_device = 'iPhone X'
        mobile_emulation = {"deviceName": __mobile_device}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        prefs = {"credentials_enable_service": False}
        chrome_options.add_experimental_option("prefs", prefs)
        caps = chrome_options.to_capabilities()

        # driver = webdriver.Chrome(desired_capabilities=caps)
        driver = webdriver.Chrome()
        
        # Start the test and set the browser's viewport size to 800x600.
        eyes.open(driver=driver, app_name='pythonAPP', test_name='pythonTEST',
                  viewport_size={'width': 1000, 'height': 800})

        # Navigate the browser to the "hello world!" web-site.
        driver.get('https://applitools.com/helloworld?diff1')

        # Visual checkpoint #1.
        eyes.check_window('Hello!')
        eyes.check("my check", Target.window().layout_regions((By.CLASS_NAME, "myClass")))

        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort_if_not_closed()
