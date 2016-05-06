# ecoding=utf-8
# Author: Sven_Weng | 翁彦彬
# Email: diandianhanbin@gmail.com
import sys

sys.path.append("..")
import config
import unittest
import random
import time
from View.Hangqing import HangQing
from View.BaseTestCase import AppTestCase


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
		self.clickHangQing()
		self.clickZiXuan()
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
		# 重启app校验是否生效
		self.reLoadApp()
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
		self.assertEqual(self.getStockNum(0), stock_num, '重启APP后置顶并未生效')

	def test008_DragToTop(self):
		"""测试拖动功能"""
		lenth = self.getLength()
		self.clickEditSelect()
		self.assertEqual(self.get_title(), u'编辑自选')
		ran = random.randint(1, lenth)
		stock_num = self.getStockNum_Bjzx(ran)
		self.dragToMove(ran)
		self.sysback()
		self.assertEqual(self.getStockNum(0), stock_num, '拖动功能不正确')
		# 重启app校验是否生效
		self.reLoadApp()
		self.assertEqual(self.getStockNum(0), stock_num, '重启APP后拖动并未生效')

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
		stock_list = [self.getStockNum(x) for x in range(self.getLength())]
		# for x in range(self.getLength()):
		# 	stock_list.append(self.getStockNum(x))
		self.assertIn(stock_num, stock_list)

		# 校验重启后是否生效
		self.reLoadApp()
		stock_list = [self.getStockNum(x) for x in range(self.getLength())]
		# for x in range(self.getLength()):
		# 	stock_list.append(self.getStockNum(x))
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
				self.assertIn(x, self.getStockNumSearch(y))
			self.inputClear()

	def test012_GuPiaoDetailAddAndDel(self):
		"""测试个股详情页面增加和删除自选"""
		ran = random.randint(0, self.getLength())
		stock_name = self.getStockName(ran)
		stock_num = self.getStockNum(ran)
		self.clickStock(ran)
		self.assertIn(stock_name, self.get_title(), '个股标题显示不正确(股票名称)')
		self.assertIn(stock_num, self.get_title(), '个股标题显示不正确(股票代码)')
		self.clickZiXuanDetail()
		self.sysback()
		self.assertEqual(self.get_title(), u'行情')
		for x in range(self.getLength()):
			self.assertNotEqual(self.getStockNum(x), stock_num)
		self.reLoadApp()  # 重启APP
		for x in range(self.getLength()):
			self.assertNotEqual(self.getStockNum(x), stock_num)

		# 添加自选
		self.clickFindStock()
		self.inputStock(stock_num)
		self.clickStockNumSearch(0)
		self.clickZiXuanDetail()
		self.sysback()
		if self.get_title() != u'行情':
			self.sysback()
		stock_list = [self.getStockNum(x) for x in range(self.getLength())]
		# for x in range(self.getLength()):
		# 	stock_list.append(self.getStockNum(x))
		self.assertIn(stock_num, stock_list)

		# 校验重启后是否生效
		self.reLoadApp()
		stock_list = [self.getStockNum(x) for x in range(self.getLength())]
		# for x in range(self.getLength()):
		# 	stock_list.append(self.getStockNum(x))
		self.assertIn(stock_num, stock_list)

	def test013_GetKXianTu(self):
		"""测试获取个股详情的K线图"""
		self.clickHangQing()
		self.assertEqual(self.get_title(), u'行情')
		ran = random.randint(0, self.getLength())
		self.clickStock(ran)
		self.clickFenShi()
		self.getScreenshot('分时', self.img_url_zixuan)
		self.clickRiK()
		self.getScreenshot('日K', self.img_url_zixuan)
		self.clickZhouK()
		self.getScreenshot('周K', self.img_url_zixuan)
		self.clickYueK()
		self.getScreenshot('月K', self.img_url_zixuan)

	def test014_CheckXinGuRiLi(self):
		"""测试获取新股日历"""
		self.clickHangQing()
		self.clickHuShen()
		self.clickXinGuRiLi()
		self.assertEqual(self.get_title(), u'新股日历')
		self.getScreenshot('新股日历', self.img_url_hushen)

	def test015_GetHuShenScreen(self):
		"""测试获取指数图片"""
		self.clickHangQing()
		self.clickHuShen()
		self.clickShangZhengZhiShu()
		self.assertIn(u'上证指数', self.get_title())
		self.getScreenshot('上证指数', self.img_url_hushen)
		self.sysback()
		self.clickShenZhengChengZhi()
		self.assertIn(u'深圳成指', self.get_title())
		self.getScreenshot('深圳成指', self.img_url_hushen)
		self.sysback()
		self.clickChuangYeBanZhi()
		self.assertIn(u'创业板指', self.get_title())
		self.getScreenshot('创业板指', self.img_url_hushen)

	def test016_GetBangKuaiInfo(self):
		"""测试获取热门行业等板块的图片"""
		self.clickHangQing()
		self.clickHuShen()
		self.clickReMenHangYe()
		self.clickZhangFuBang()
		self.clickDieFuBang()
		self.clickHuanShouBang()
		self.clickZhenFuBang()
		ranks = ['热门行业', '涨幅榜', '跌幅榜', '换手榜', '振幅榜']
		for x, rank in enumerate(ranks):
			self.clickGetMore(x)
			self.getScreenshot(rank, self.img_url_hushen)
			self.sysback()

	def test017_GetMoreShoot(self):
		"""测试获取更多的入口截图"""
		self.clickHangQing()
		self.clickMore()
		dataone = [self.more_hushen, self.more_zhaiquan, self.more_jijin]
		datatwo = [self.more_ganggu, self.more_quanqiu, self.more_qihuo]
		for x in dataone:
			for y in x:
				self.driver.find_element_by_name(y).click()
				self.getScreenshot(y, self.img_url_more)
				self.sysback()
		self.swipe_to_up()
		for a in datatwo:
			for b in a:
				self.driver.find_element_by_name(b).click()
				self.getScreenshot(b, self.img_url_more)
				self.sysback()

	def test018_BuyStock(self):
		"""测试购买股票"""
		self.clickHangQing()
		while True:
			ran = random.randint(0, self.getLength())
			stock_num = self.getStockNum(ran)
			self.clickStock(ran)
			try:
				self.clickBuy()
				break
			except Exception:
				self.sysback()
		self.assertEqual(self.get_title(), u'交易登录')
		while True:
			self.ZiJinZhangHaoLogin()
			time.sleep(20)
			if self.get_title() != u'交易登录':
				break
		self.clickThird(0)
		self.clickBuyBtn()
		# 进入委托买入页面点击买入,同样适用name方法寻找按钮
		self.clickBuyBtn()
		time.sleep(5)
		self.assertIn(u'委托请求发送成功', self.getRstMsg())


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(HangQingTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
