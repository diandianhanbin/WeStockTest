# ecoding=utf-8
# Author: Sven_Weng | 翁彦彬
# Email: diandianhanbin@gmail.com
import sys
sys.path.append("..")  # 保证上级config的引用
import unittest
import json
import config
import time
import random
from View.Hangqing import HangQing
from View.BaseTestCase import AppTestCase
from selenium.webdriver.common.by import By


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

	def test005_ZhangDieFuChange(self):
		"""测试涨跌幅的点击变动"""
		self.assertEqual(self.getZhangDieChange(), u'涨跌幅')
		self.clickZhangDieFuChange()
		self.assertEqual(self.getZhangDieChange(), u'涨跌值')
		self.clickZhangDieFuChange()
		self.assertEqual(self.getZhangDieChange(), u'成交额')
		self.clickZhangDieFuChange()
		self.assertEqual(self.getZhangDieChange(), u'涨跌幅')

	# ---------------测试编辑自选页面--------------------

	def test006_DeleteZiXuan(self):
		"""测试删除自选"""
		lenth = self.getLength()
		self.clickEditSelect()
		self.assertEqual(self.get_title(), u'编辑自选')
		ran = random.randint(1, lenth)
		stock_num = self.getStockNum_Bjzx(ran)
		self.clickDelete(ran)
		self.sysback()
		for x in range(self.getLength()):
			self.assertNotEqual(self.getStockNum(x), stock_num)

	def test007_SetTop(self):
		"""测试置顶自选"""
		lenth = self.getLength()
		self.clickEditSelect()
		self.assertEqual(self.get_title(), u'编辑自选')
		ran = random.randint(1, lenth)
		stock_num = self.getStockNum_Bjzx(ran)
		self.clickSetTop(ran)
		self.sysback()
		self.assertEqual(self.getStockNum(0), stock_num)
		# 重启app校验是否生效
		self.reLoadApp()
		self.assertEqual(self.getStockNum(0), stock_num, u'重启APP后置顶并未生效')

	def test008_DragToTop(self):
		"""测试拖动功能"""
		lenth = self.getLength()
		self.clickEditSelect()
		self.assertEqual(self.get_title(), u'编辑自选')
		ran = random.randint(1, lenth)
		stock_num = self.getStockNum_Bjzx(ran)
		self.dragToMove(ran)
		self.sysback()
		self.assertEqual(self.getStockNum(0), stock_num, u'拖动功能不正确')
		# 重启app校验是否生效
		self.reLoadApp()
		self.assertEqual(self.getStockNum(0), stock_num, u'重启APP后拖动并未生效')

	def test009_AddAndDelStock(self):
		"""测试删除自选和添加自选"""
		# 删除自选
		while True:
			ran = random.randint(0, self.getLength())
			stock_num = self.getStockNum(ran)
			try:
				int(stock_num)
				break
			except ValueError:
				pass
		print stock_num
		self.clickFindStock()  # 切换到查找页面
		self.inputStock(stock_num)
		self.clickAddOrDel(0)
		self.sysback()
		if self.get_title() != u'行情':
			self.sysback()
		for x in range(self.getLength()):
			self.assertNotEqual(stock_num, self.getStockNum(x))

		# 校验重启后是否生效
		self.reLoadApp()
		for x in range(self.getLength()):
			self.assertNotEqual(stock_num, self.getStockNum(x))

		# 添加自选
		self.clickFindStock()  # 切换到查找页面
		self.inputStock(stock_num)
		self.clickAddOrDel(0)
		self.sysback()
		if self.get_title() != u'行情':
			self.sysback()
		stock_list = []
		for x in range(self.getLength()):
			stock_list.append(self.getStockNum(x))
		self.assertIn(stock_num, stock_list)

		# 校验重启后是否生效
		self.reLoadApp()
		stock_list = []
		for x in range(self.getLength()):
			stock_list.append(self.getStockNum(x))
		self.assertIn(stock_num, stock_list)

	def test010_CleanHistory(self):
		"""测试清除历史记录"""
		self.clickHangQing()
		self.clickFindStock()
		if self.clickClean('text') == u'股票代码不存在':
			self.inputStock('600000')
			self.clickStockNumSearch(0)
			self.sysback()
			self.clickFindStock()
			self.clickClean('click')
			self.clickEnsure()
			self.assertEqual(self.clickClean('text'), u'股票代码不存在')
		elif self.clickClean('text') == u'清除搜索历史':
			self.clickClean('click')
			self.clickEnsure()
			self.assertEqual(self.clickClean('text'), u'股票代码不存在')

	def test011_NumSearch(self):
		"""测试股票编号搜索逻辑"""
		stock_prefix = ['600', '300', '000', '002']
		self.clickHangQing()
		self.clickFindStock()
		for x in stock_prefix:
			self.inputStock(x)
			self.sysback()
			for y in range(self.getLengthSearch()):
				print x, ' | ', self.getStockNumSearch(y)
				self.assertIn(x, self.getStockNumSearch(y))
			self.inputClear()


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(HangQingTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
