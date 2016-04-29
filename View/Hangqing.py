# ecoding=utf-8
# Author: Sven_Weng | 翁彦彬
# Email: diandianhanbin@gmail.com
from django.forms.widgets import Input

import config
import random
from selenium.webdriver.common.by import By
from View.BaseView import AppUI


class HangQing(AppUI):

	# ----------------------行情所有数据------------------------------------
	native_hangqing = config.COMMON['native_hangqing']
	ensure = config.COMMON['ensure']

	# ----------------------自选页面---------------------------
	edit_select = config.HANGQING['edit_select']
	find_stock = config.HANGQING['find_stock']
	stock_info = config.HANGQING['stock']['info']
	zixuan = config.HANGQING['zixuan']
	stock_num = config.HANGQING['stock']['num']
	stock_name = config.HANGQING['stock']['name']
	mingchengdaima = config.HANGQING['mingchendaima']
	newprice = config.HANGQING['newprice']
	stock_price = config.HANGQING['price']
	zhangdiefuchange = config.HANGQING['newzhangdiefu']
	zhangdiefu = config.HANGQING['zhangdiefu']

	# ----------------------编辑自选页面----------------------
	delete = config.HANGQING['delete']
	settop = config.HANGQING['settop']
	drag = config.HANGQING['move']
	drag_title = config.HANGQING['move_title']
	stock_num_bjzx = config.HANGQING['stock_num']

	# ----------------------查找股票页面----------------------
	input_area = config.HANGQING['input']
	stock_name_search = config.HANGQING['stock_name_search']
	stock_num_search = config.HANGQING['stock_num_search']
	addordel = config.HANGQING['addordel_stock']
	clean_history = config.HANGQING['clean_history']

	# ----------------------个股详情页面----------------------
	zixuan_detail = config.HANGQING['zixuan_stock_detail']

	# ----------------------执行方法---------------------------------------
	# ----------------------自选页面-----------------------------

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

	def getStockName(self, index):
		"""
		根据序号获取自选页面股票名称
		:param index: int, 序号
		:return: str, 股票代码
		"""
		if isinstance(index, int):
			stock_name = self.find_elements(*self.stock_name)[index].text
			return stock_name
		else:
			print '输入类型有误'

	def getStockNum(self, index):
		"""
		根据序号获取自选页面股票代码
		:param index: int, 序号
		:return: str,股票代码
		"""
		if isinstance(index, int):
			stock_num = self.find_elements(*self.stock_num)[index].text
			return stock_num
		else:
			print '输入类型有误'

	def clickStock(self, index):
		"""
		根据序号点击自选页面个股进入个股详情
		:param index: int, 序号
		:return: None
		"""
		if isinstance(index, int):
			self.find_elements(*self.stock_name)[index].click()
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

# ---------------编辑自选页面-------------------------------

	def clickDelete(self, index):
		"""
		根据序号点击删除按钮
		:param index:序号
		:return: None
		"""
		if isinstance(index, int):
			self.find_elements(*self.delete)[index].click()
		else:
			print "输入类型有误"

	def clickSetTop(self, index):
		"""
		根据序号点击置顶按钮
		:param index: 序号
		:return: None
		"""
		if isinstance(index, int):
			self.find_elements(*self.settop)[index].click()
		else:
			print "输入类型有误"

	def dragToMove(self, index):
		"""
		根据序号拖动相关个股到'拖动'位置(置顶)
		:param index: 序号
		:return: None
		"""
		if isinstance(index, int):
			start = self.find_elements(*self.drag)[index]
			end = self.find_element(*self.drag_title)
			self.driver.drag_and_drop(start, end)
		else:
			print "输入类型有误"

	def getStockNum_Bjzx(self, index):
		if isinstance(index, int):
			rst = self.find_elements(*self.stock_num_bjzx)[index].text
			return rst
		else:
			print "输入类型有误"

# ------------查找股票页面-----------

	def inputStock(self, val):
		"""
		在查找股票页面输入内容
		:param val: str, 输入的内容
		:return: None
		"""
		self.find_element(*self.input_area).send_keys(val)

	def inputClear(self):
		"""
		在查找股票页面清除输入框的内容
		:return: None
		"""
		self.find_element(*self.input_area).clear()

	def getStockNameSearch(self, index):
		"""
		根据传入的序号获取搜索结果的股票名称
		:param index: 序号
		:return:str, 股票名称
		"""
		rst = self.find_elements(*self.stock_name_search)[index].text
		return rst

	def getStockNumSearch(self, index):
		"""
		根据传入的序号获取搜索结果的股票代码
		:param index:序号
		:return:str, 股票代码
		"""
		rst = self.find_elements(*self.stock_num_search)[index].text
		return rst

	def clickStockNumSearch(self, index):
		"""
		根据传入的序号点击相应的搜索结果
		:param index: 序号
		:return:None
		"""
		self.find_elements(*self.stock_num_search)[index].click()

	def clickAddOrDel(self, index):
		"""
		根据传入的序号点击添加删除按钮
		:param index:序号
		:return:None
		"""
		self.find_elements(*self.addordel)[index].click()

	def clickClean(self, val):
		"""
		根据传入的val判定点击或者获取文本
		:param val: str, [click,点击] [text,获取文本]
		:return:str, 获取的文本
		"""
		if val == 'click':
			self.find_element(*self.clean_history).click()
		elif val == 'text':
			rst = self.find_element(*self.clean_history).text
			return rst
		else:
			print 'clickClean函数的入参有误'

	def clickEnsure(self):
		"""
		点击确定按钮
		:return:None
		"""
		self.find_element(*self.ensure).click()

	def getLengthSearch(self):
		"""
		获取个股搜索页面的长度
		:return: int, 搜索页面的长度
		"""
		rst = len(self.find_elements(*self.stock_num_search))
		return rst

	# --------------个股详情页面------------------

	def clickZiXuanDetail(self):
		"""
		点击个股详情页面的自选按钮
		:return: None
		"""
		self.find_element(*self.zixuan_detail).click()