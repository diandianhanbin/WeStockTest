# ecoding=utf-8
# Author: Sven_Weng | 翁彦彬
# Email: diandianhanbin@gmail.com
import unittest
from appium import webdriver
# from selenium import webdriver
import config


#
# class BaseTestCase(unittest.TestCase):
# 	def setUp(self):
# 		self.driver = webdriver.Firefox()
# 		self.driver.maximize_window()
# 		self.driver.get('http://www.baidu.com')
# 		self.driver.implicitly_wait(30)
#
# 	def tearDown(self):
# 		self.driver.quit()


class AppTestCase(unittest.TestCase):
	def setUp(self):
		desired_caps = {
			'platformName': config.CONNECT['platformName'],
			'platformVersion': config.CONNECT['platformVersion'],
			'deviceName': config.CONNECT['deviceName'],
			'appPackage': config.CONNECT['appPackage'],
			'appActivity': config.CONNECT['appActivity']
		}
		self.driver = webdriver.Remote(config.CONNECT['baseUrl'], desired_caps)

	def tearDown(self):
		self.driver.quit()

	# def get_driver(self):
	# 	return self.driver

