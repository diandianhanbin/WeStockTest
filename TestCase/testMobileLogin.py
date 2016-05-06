# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : diandianhanbin@gmail.com

import sys

from View.BaseTestCase import AppTestCase

sys.path.append("..")  # 保证上级config的引用
import unittest
import config
from appium import webdriver
import time
from View.MobileLogin import MobileLogin


class YinDao(AppTestCase, MobileLogin):

	def test001_swipe(self):
		for x in range(5):
			self.swipe_to_left()


class Login(unittest.TestCase, MobileLogin):
	def setUp(self):
		desired_caps = {
			'platformName': config.CONNECT['platformName'],
			'platformVersion': config.CONNECT['platformVersion'],
			'deviceName': config.CONNECT['deviceName'],
			'appPackage': config.CONNECT['appPackage'],
			'appActivity': config.CONNECT['loginActivity']
		}
		self.driver = webdriver.Remote(config.CONNECT['baseUrl'], desired_caps)

	def tearDown(self):
		self.driver.quit()


	def test001_login(self):
		self.driver.hide_keyboard()
		self.sendUserName(config.MOBILELOGIN['username'])
		self.sendPassWord(config.MOBILELOGIN['password'])
		self.clickLoginBtn()
		self.assertEqual(self.get_title(), u'行情')


if __name__ == '__main__':
	suite1 = unittest.TestLoader().loadTestsFromTestCase(YinDao)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(Login)
	alltest = unittest.TestSuite([suite2])
	unittest.TextTestRunner(verbosity=2).run(alltest)