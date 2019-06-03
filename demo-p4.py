import os

from selenium import webdriver
from applitools.selenium.eyes import Eyes
from applitools.common import BatchInfo

class HelloWorld:

    eyes = Eyes() # eyes-selenium 3.16.2 / selenium 3.141.0
    
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']

    try:
        
        # Open a Chrome browser.
        driver = webdriver.Chrome()
        
        # Start the test and set the browser's viewport size to 800x600.
        eyes.open(driver=driver, app_name='pythonAPP', test_name='pythonTEST',
                  viewport_size={'width': 1000, 'height': 800})

        b = BatchInfo(id="pythonID", name="pythonNAME")
        b.id = "pythonID"

        eyes.batch = b

        # Navigate the browser to the "hello world!" web-site.
        driver.get('https://applitools.com/helloworld?diff1')

        # Visual checkpoint #1.
        eyes.check_window('Hello!')

        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort_if_not_closed()
