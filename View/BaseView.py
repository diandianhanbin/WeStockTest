# ecoding=utf-8
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time as t

__author__ = "Sven_Weng"


# class Factory(object):
# 	def __init__(self, driver):
# 		self.driver = driver
#
# 	# 工厂方法
# 	def createWebDdriver(self, webDdriver):
# 		if webDdriver == 'web':
# 			return WebUI(self.driver)
# 		elif webDdriver == 'app':
# 			return AppUI(self.driver)


class WebDdriver(object):
	def __init__(self, driver):
		self.driver = driver

	def __str__(self):
		return 'webDdriver'

	def find_element(self, *loc):
		try:
			element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
			return element
		except NoSuchElementException, e:
			print 'Error details :%s' % (e.args[0])

	def find_elements(self, *loc):
		try:
			# return self.driver.find_elements(*loc)
			elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
			return elements
		except NoSuchElementException, e:
			print 'Error details :%s' % (e.args[0])

	@property
	def wait(self):
		t.sleep(5)

	def getScreenshot(self, name, url, form='png'):
		t.sleep(2)
		self.driver.get_screenshot_as_file(url + name + "." + form)


class WebUI(WebDdriver):
	def __str__(self):
		return 'WEB UI'


class AppUI(WebDdriver):
	def __str__(self):
		return 'App UI'
