# ecoding=utf-8
# Author: Sven_Weng翁彦彬
# Email: diandianhanbin@gmail.com
from django.forms.widgets import Input

import config
import random
from selenium.webdriver.common.by import By
from View.BaseView import AppUI


class HangQing(AppUI):

	# ----------------------行情所有数据--------------------------
	native_hangqing = config.COMMON['native_hangqing']

	edit_select = config.HANGQING['edit_select']
	find_stock = config.HANGQING['find_stock']
	stock_info = config.HANGQING['stock']['info']
	zixuan = config.HANGQING['zixuan']
	stock_num = config.HANGQING['stock']['num']
	mingchengdaima = config.HANGQING['mingchendaima']
	newprice = config.HANGQING['newprice']
	stock_price = config.HANGQING['price']
	zhangdiefuchange = config.HANGQING['newzhangdiefu']
	zhangdiefu = config.HANGQING['zhangdiefu']

	# ----------------------------------------------------------

	# ----------------------执行方法-----------------------------

	def clickHangQing(self):
		"""
		点击导航栏的行情按钮
		:return: None
		"""
		self.find_element(*self.native_hangqing).click()

	def clickEditSelect(self):
		"""
		点击编辑自选,进入编辑自选页面
		:return: None
		"""
		self.find_elements(*self.edit_select)[0].click()

	def clickFindStock(self):
		"""
		点击放大镜,进入查询自选股界面
		:return: None
		"""
		self.find_elements(*self.edit_select)[1].click()

	def clickZiXuan(self):
		"""
		点击行情页面的自选
		:return: None
		"""
		if self.get_title() != u'行情':
			try:
				self.clickHangQing()
			except Exception as e:
				print e
				print '行情导航栏无法点击,请检查APP的状态'
		else:
			self.find_element(*self.zixuan).click()

	def getLength(self):
		"""
		获取自选页面个股的数量
		:return:int, 自选页面个股的数量
		"""
		rst = len(self.find_elements(*self.stock_info))
		return rst

	def clickNameNum(self):
		"""
		点击自选页面的名称代码
		:return: None
		"""
		self.clickZiXuan()
		self.find_element(*self.mingchengdaima).click()

	def getStockNum(self, index):
		"""
		根据序号获取股票代码
		:param index: int, 序号
		:return: str,股票代码
		"""
		if isinstance(index, int):
			stock_num = self.find_elements(*self.stock_num)[index].text
			return stock_num
		else:
			print '输入类型有误'

	def clickNewPrice(self):
		"""
		点击最新价按钮
		:return: None
		"""
		self.find_element(*self.newprice).click()

	def getStockPrice(self, index):
		"""
		根据序号获取股票最新价
		:param index: int, 序号
		:return: None
		"""
		if isinstance(index, int):
			stock_price = self.find_elements(*self.stock_price)[index].text
			return stock_price
		else:
			print "输入类型有误"

	def clickZhangDieFuChange(self):
		"""
		点击自选的涨跌幅
		:return: None
		"""
		self.find_elements(*self.zhangdiefuchange)[0].click()

	def getZhangDieChange(self):
		"""
		获取涨跌幅变动的文本
		:return: str, 涨跌幅变动的文本
		"""
		rst = self.find_element(*self.zhangdiefu).text
		return rst