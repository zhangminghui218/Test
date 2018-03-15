
# _*_ coding :utf-8 _*_

from appium import webdriver
from time import sleep
import subprocess

import unittest

desired_caps = {
    'platformName':'Android',
    'deviceName':'emulator-5554',
    'platformVersion':'4.2',
    'appPackage':'com.youku.phone',
    'appActivity':'com.youku.ui.activity.HomePageActivity'

}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

sleep(5)
driver.find_element_by_id()