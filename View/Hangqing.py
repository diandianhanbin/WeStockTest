# ecoding=utf-8
# Author: Sven_Weng | 翁彦彬
# Email: diandianhanbin@gmail.com

import config
import random
from selenium.webdriver.common.by import By
from View.BaseView import AppUI


class HangQing(AppUI):

	# ----------------------行情所有数据------------------------------------
	native_hangqing = config.COMMON['native_hangqing']
	ensure = config.COMMON['ensure']
	img_url = config.HANGQING['imgurl']
	img_url_zixuan = config.HANGQING['imgurl_zixuan']
	img_url_hushen = config.HANGQING['imgurl_hushen']
	img_url_ganggu = config.HANGQING['imgurl_ganggu']
	img_url_more = config.HANGQING['imgurl_more']

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
	fenshi = config.HANGQING['fenshi']
	rik = config.HANGQING['rik']
	zhouk = config.HANGQING['zhouk']
	yuek = config.HANGQING['yuek']
	buy = config.HANGQING['buy_detail']
	sale = config.HANGQING['sale_detail']

	# ----------------------沪深页面-------------------------
	hushen = config.HANGQING['hushen']
	xingurili = config.HANGQING['xingurili']
	shangzhengzhishu = config.HANGQING['shangzhengzhishu']
	shenzhengchengzhi = config.HANGQING['shengzhengchengzhi']
	chuangyebanzhi = config.HANGQING['chuangyebanzhi']
	getmore = config.HANGQING['getmore']
	remenhangye = config.HANGQING['remenhangye']
	zhangfubang = config.HANGQING['zhangfubang']
	diefubang = config.HANGQING['diefubang']
	huanshoubang = config.HANGQING['huanshoubang']
	zhenfubang = config.HANGQING['zhenfubang']

	# ----------------------港股页面-------------------------
	ganggutongzhangfubang = config.HANGQING['ganggutongzhangfubang']
	ganggutongdiefubang = config.HANGQING['ganggutongdiefubang']
	zhubanzhangfubang = config.HANGQING['zhubangzhangfubang']
	zhubandiefubang = config.HANGQING['zhubangdiefubang']
	remenahgu = config.HANGQING['remenahgu']
	hongchougu = config.HANGQING['hongchougu']
	lanchougu = config.HANGQING['lanchougu']

	# ----------------------更多页面-------------------------
	more_hushen = config.HANGQING['more_hushen']
	more_zhaiquan = config.HANGQING['more_zhaiquan']
	more_jijin = config.HANGQING['more_jijin']
	more_ganggu = config.HANGQING['more_ganggu']
	more_quanqiu = config.HANGQING['more_quanqiu']
	more_qihuo = config.HANGQING['more_qihuo']
	more = config.HANGQING['gengduo']

	# ---------委托买入卖出页面-----------------
	trust_edit = config.HANGQING['entrust_edit']
	third_btn = config.HANGQING['third']
	buy_btn = config.HANGQING['buy_btn']
	rst_msg = config.HANGQING['rst_msg']
	enter = config.HANGQING['enter']

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

	def clickFenShi(self):
		"""
		点击个股详情的分时
		:return:None
		"""
		self.find_element(*self.fenshi).click()

	def clickRiK(self):
		"""
		点击个股详情的日K
		:return: None
		"""
		self.find_element(*self.rik).click()

	def clickZhouK(self):
		"""
		点个股详情的击周K
		:return: None
		"""
		self.find_element(*self.zhouk).click()

	def clickYueK(self):
		"""
		点击个股详情的月K
		:return: None
		"""
		self.find_element(*self.yuek).click()

	def clickBuy(self):
		"""
		点击买入按钮
		:return: None
		"""
		self.find_element(*self.buy).click()

	def clickSale(self):
		"""
		点击卖出按钮
		:return: None
		"""
		self.find_element(*self.sale).click()

	# ---------------沪深页面-------------------

	def clickHuShen(self):
		"""
		点击沪深
		:return:None
		"""
		self.find_element(*self.hushen).click()

	def clickXinGuRiLi(self):
		"""
		点击新股日历
		:return: None
		"""
		self.find_element(*self.xingurili).click()

	def clickShangZhengZhiShu(self):
		"""
		点击上证指数
		:return: None
		"""
		self.find_element(*self.shangzhengzhishu).click()

	def clickShenZhengChengZhi(self):
		"""
		点击深圳成指
		:return: None
		"""
		self.find_element(*self.shenzhengchengzhi).click()

	def clickChuangYeBanZhi(self):
		"""
		点击创业板指
		:return: None
		"""
		self.find_element(*self.chuangyebanzhi).click()

	def clickGetMore(self, index):
		"""
		根据传入的序号点击查看全部按钮(查看沪深板块的全部信息,热门板块,涨幅榜等)
		:param index: 序号
		:return: None
		"""
		self.find_elements(*self.getmore)[index].click()

	def clickReMenHangYe(self):
		"""
		点击热门行业
		:return:None
		"""
		self.find_element(*self.remenhangye).click()

	def clickZhangFuBang(self):
		"""
		点击涨幅榜
		:return: None
		"""
		self.find_element(*self.zhangfubang).click()

	def clickDieFuBang(self):
		"""
		点击跌幅榜
		:return: None
		"""
		self.find_element(*self.diefubang).click()

	def clickHuanShouBang(self):
		"""
		点击换手榜
		:return: None
		"""
		self.find_element(*self.huanshoubang).click()

	def clickZhenFuBang(self):
		"""
		点击振幅榜
		:return: None
		"""
		self.find_element(*self.zhenfubang).click()

	# ---------------港股页面-------------------

	def clickGangGuTongZhangFuBang(self):
		"""
		点击港股通涨幅榜
		:return: None
		"""
		self.find_element(*self.ganggutongzhangfubang).click()

	def clickGangGuTongDieFuBang(self):
		"""
		点击港股通跌幅榜
		:return: None
		"""
		self.find_element(*self.ganggutongdiefubang).click()

	def clickZhuBangZhangFuBang(self):
		"""
		点击主板涨幅榜
		:return:None
		"""
		self.find_element(*self.zhubanzhangfubang).click()

	def clickZhuBangDieFuBang(self):
		"""
		点击主板跌幅榜
		:return: None
		"""
		self.find_element(*self.zhubandiefubang).click()

	def clickReMenAHGu(self):
		"""
		点击热门AH股
		:return: None
		"""
		self.find_element(*self.remenahgu).click()

	def clickHongChouGu(self):
		"""
		点击红筹股
		:return: None
		"""
		self.find_element(*self.hongchougu).click()

	def clickLanChouGu(self):
		"""
		点击蓝筹股
		:return: None
		"""
		self.find_element(*self.lanchougu).click()

	# ---------------更多页面-------------------

	def clickMore(self):
		"""
		点击更多
		:return: None
		"""
		self.find_element(*self.more).click()

	# ---------委托买入卖出页面-----------------

	def clickThird(self, index):
		"""
		点击委托买入卖出页面的三分之一按钮
		:param: 序号,0表示三分之一
		:return: None
		"""
		self.find_elements(*self.third_btn)[index].click()

	def clickBuyBtn(self):
		"""
		点击委托买入按钮
		:return: None
		"""
		self.find_element(*self.buy_btn).click()

	def getRstMsg(self):
		"""
		获取返回的信息
		:return:str, 获取返回状态信息
		"""
		rst = self.find_element(*self.rst_msg).text
		return rst

	def clickEnter(self):
		"""
		点击确定按钮
		:return: None
		"""
		self.find_element(*self.enter).click()