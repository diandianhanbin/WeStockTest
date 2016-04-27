# ecoding=utf-8
import sys
sys.path.append("..")  # 保证上级config的引用
import unittest
import json
import config
import time
from View.Hangqing import HangQing
from View.BaseTestCase import AppTestCase
from selenium.webdriver.common.by import By
__author__ = "Sven_Weng"


class HangQingTest(AppTestCase, HangQing):

	# ---------------测试自选页面--------------------
	def test001_JiangXu(self):
		"""测试自选页面降序排列"""
		num = self.getLength() - 1
		self.clickNameNum()
		a = 999999
		for x in range(num):
			try:
				int(self.getStockNum(x))
				self.assertTrue(int(a) > int(self.getStockNum(x)))
				a = self.getStockNum(x)
			except ValueError:
				pass

	def test002_ShengXu(self):
		"""测试自选页面升序排列"""
		num = self.getLength() - 1
		self.clickNameNum()
		self.clickNameNum()
		a = 0
		for x in range(num):
			try:
				int(self.getStockNum(x))
				self.assertTrue(int(a) < int(self.getStockNum(x)))
				a = self.getStockNum(x)
			except ValueError:
				pass

	def test003_PriceJiangXu(self):
		"""测试最新价降序排列"""
		num = self.getLength() - 1
		self.clickNewPrice()
		a = 99999
		for x in range(num):
			try:
				float(self.getStockPrice(x))
				self.assertTrue(float(a) > float(self.getStockPrice(x)))
				a = self.getStockPrice(x)
			except ValueError:
				pass

	def test004_PriceShengXu(self):
		"""测试最新价升序排列"""
		num = self.getLength() - 1
		self.clickNewPrice()
		self.clickNewPrice()
		a = 0
		for x in range(num):
			try:
				float(self.getStockPrice(x))
				self.assertTrue(float(a) < float(self.getStockPrice(x)))
				a = self.getStockPrice(x)
			except ValueError:
				pass

	def test004_ZhangDieFuChange(self):
		"""测试涨跌幅的点击变动"""
		self.assertEqual(self.getZhangDieChange(), u'涨跌幅')
		self.clickZhangDieFuChange()
		self.assertEqual(self.getZhangDieChange(), u'涨跌值')
		self.clickZhangDieFuChange()
		self.assertEqual(self.getZhangDieChange(), u'成交额')
		self.clickZhangDieFuChange()
		self.assertEqual(self.getZhangDieChange(), u'涨跌幅')


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(HangQingTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
