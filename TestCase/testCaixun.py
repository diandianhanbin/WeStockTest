# ecoding=utf-8
import unittest
import json
import config
import time
from View.Caixun import Caixun
from View.BaseTestCase import AppTestCase
from selenium.webdriver.common.by import By
__author__ = "Sven_Weng"


class CaixunTest(AppTestCase, Caixun):

	def testClickTitle(self):
		"""测试财讯的频道内容是否正确"""
		self.clickCaixun()
		self.assertEqual(self.get_title(), u'财讯')
		self.clickTuijian()
		self.get_screen('tuijian')
		self.clickNeirong()
		self.get_screen('tuijianneirong')
		self.sysback()
		self.clickGupiao()
		self.get_screen('gupiao')
		self.clickNeirong()
		self.get_screen('gupiaoneirong')
		self.sysback()
		self.clickJijin()
		self.get_screen('jijin')
		self.clickNeirong()
		self.get_screen('jijinneirong')
		self.sysback()
		self.clickZhaiquan()
		self.get_screen('zhaiquan')
		self.clickNeirong()
		self.get_screen('zhaiquanneirong')
		self.sysback()
		self.clickXinsanban()
		self.get_screen('xinsanban')
		self.clickNeirong()
		self.get_screen('xinsanbanneirong')

	def testAddPindao(self):
		"""测试增加频道功能"""
		self.clickCaixun()
		self.clickPlus()
		self.assertEqual(self.get_title(), u'频道管理')
		# 校验推荐不可点击
		self.assertFalse(self.checkTuijianEnabled())
		# 校验其他可以点击
		self.assertTrue(self.checkOtherAbled())

		text = self.clickTextItem()
		self.assertEqual(text, self.getFifthItemText())
		self.clickItem(5)

	def testNewPindao(self):
		"""测试新增频道内容显示"""
		self.clickCaixun()
		self.clickPlus()
		text = self.clickTextItem()
		self.sysback()
		ori = self.getLocation(*config.CAIXUN['xinsanban'])
		new = self.getLocation(*config.CAIXUN['tuijian'])
		self.driver.swipe(ori[0], ori[1], new[0], new[1])
		self.find_element(*(By.NAME, text)).click()
		self.clickNeirong()
		self.get_screen(text)


if __name__ == '__main__':
	unittest.main(verbosity=2)
