import os

from selenium import webdriver
from selenium.webdriver import Firefox
from applitools.selenium.eyes import Eyes
from applitools.selenium.eyes import Target
from applitools.common import Region
from applitools.common.config import SeleniumConfiguration, StitchMode
from applitools.selenium import BatchInfo
from selenium.webdriver.common.by import By
from applitools.common import logger
from applitools.common.logger import StdoutLogger

class HelloWorld:
    logger.set_logger(StdoutLogger())

try:
    driver = webdriver.Firefox()
    driver.get('https://www.goodrx.com/xarelto/what-is')


    eyes = Eyes()
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']
    eyes.configuration.stitch_mode = StitchMode.CSS
    eyes.open(driver=driver, app_name='Zachs Python app', test_name='I_29263 FF CSS transition',
                viewport_size={'width': 1000, 'height': 800})
    
    prosconsEle = driver.find_element_by_xpath('//*[@id="pros-cons"]/..')
    eyes.check("pros-cons", Target.region(prosconsEle))

    warningsEle = driver.find_element_by_xpath('//*[@id="warnings"]/..')
    eyes.check("warnings", Target.region(warningsEle))

    eyes.close()

finally:
    eyes.abort_if_not_closed()
    driver.quit()