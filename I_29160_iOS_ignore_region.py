import os
from selenium import webdriver
from applitools.selenium.eyes import Eyes
from applitools.selenium.eyes import Target
from selenium.webdriver.common.by import By

class HelloWorld:

    # Initialize the eyes SDK and set your private API key.
    eyes = Eyes()
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']

    # Set the desired capapbilities.
    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['browserName'] = 'Safari'
    desired_caps['deviceName'] = 'iPhone XR'
    desired_caps['platformVersion'] = '12.2'
    desired_caps['automationName'] = 'XCUITest'  # Possible to run without.

    # Open browser
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    try:

        # Start the test.
        eyes.open(driver=driver, app_name='Zachs pythonAPP',
                  test_name='python 4.0.5 ignore region misplacement')

        # Navigate the browser to the "Hello World!" web-site.
        driver.get('https://applitools.com/helloworld?diff1')

        # Visual validation point #1.
        # eyes.check_window('Hello!')
        # eyes.check("winning", Target.window())

        eyes.check("ignore random number", Target.window().ignore((By.CLASS_NAME, "random-number")))

        # Click the "Click me!" button.
        # driver.find_element_by_tag_name('button').click()

        # Visual validation #2.
        # eyes.check_window('Click!')

        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.Close was called, end the test as aborted.
        eyes.abort_if_not_closed()
