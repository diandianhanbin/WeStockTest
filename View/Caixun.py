# ecoding=utf-8
import time

from django.forms.widgets import Input

import config
import random
from selenium.webdriver.common.by import By
from View.BaseView import AppUI
__author__ = "Sven_Weng"


class Caixun(AppUI):

	# ----------------------财讯所有数据--------------------------
	native_caixun = config.COMMON['native_caixun']

	tuijian = config.CAIXUN['tuijian']
	gupiao = config.CAIXUN['gupiao']
	jijin = config.CAIXUN['jijin']
	zhaiquan = config.CAIXUN['zhaiquan']
	xinsanban = config.CAIXUN['xinsanban']
	neirong = config.CAIXUN['zixunneirong']
	plusbtn = config.CAIXUN['jiahao']
	pindao = config.CAIXUN['pindao']

	img_url = config.CAIXUN['imgurl']

	back = config.CAIXUN['back']

	# ----------------------------------------------------------

	# ---------------------执行方法------------------------------

	def clickCaixun(self):
		"""
		点击底部导航的财讯
		:return:None
		"""
		self.find_element(*self.native_caixun).click()
		time.sleep(2)

	def get_screen(self, name):
		"""
		对当前屏幕截图,函数中调用了getScreenshot,在上方定义常量的时候必须定义img_url
		:param name: 保存图片的名称
		:return:None
		"""
		self.getScreenshot(name, self.img_url)

	def clickTuijian(self):
		"""
		点击推荐
		:return: None
		"""
		self.find_element(*self.tuijian).click()

	def clickGupiao(self):
		"""
		点击股票
		:return: None
		"""
		self.find_element(*self.gupiao).click()

	def clickJijin(self):
		"""
		点击基金
		:return: None
		"""
		self.find_element(*self.jijin).click()

	def clickZhaiquan(self):
		"""
		点击债券
		:return: None
		"""
		self.find_element(*self.zhaiquan).click()

	def clickXinsanban(self):
		"""
		点击新三板
		:return: None
		"""
		self.find_element(*self.xinsanban).click()

	def clickNeirong(self):
		"""
		点击每个财讯版面的第一条记录
		:return: None
		"""
		self.find_elements(*self.neirong)[0].click()

	def clickPlus(self):
		"""
		点击财讯标题的加号,进入频道管理页面
		:return: None
		"""
		self.find_elements(*self.plusbtn)[0].click()

	def checkTuijianEnabled(self):
		"""
		检查推荐是否可用,可用返回True,不可用返回False
		:return: True/False
		"""
		rst = self.find_elements(*self.pindao)[0].is_enabled()
		return rst

	def checkOtherAbled(self):
		"""
		检查频道的非推荐频道是否可点击,可用返回True,不可用返回False
		:return: True/False
		"""
		rst = self.find_elements(*self.pindao)[random.randint(1, 10)].is_enabled()
		return rst

	def getLenth(self):
		"""
		获取频道的数量
		:return: int, 频道的数量
		"""
		rst = len(self.find_elements(*self.pindao))
		return rst

	def clickTextItem(self):
		"""
		点击频道管理下方的随机一个频道,并且保存这个频道的名称,调用前请确保我的频道中只有[推荐,股票,基金,债券,新三板]
		:return: str, 频道的名称
		"""
		ran = random.randint(5, self.getLenth())
		text = self.find_elements(*self.pindao)[ran].text
		self.find_elements(*self.pindao)[ran].click()
		return text

	def getFifthItemText(self):
		"""
		获取第五个项目的名称
		:return: str, 第五个项目的名称
		"""
		text = self.find_elements(*self.pindao)[5].text
		return text

	def clickItem(self, num):
		"""
		点击某个频道
		:param num: int, 频道的编号
		:return: None
		"""
		if isinstance(num, int):
			self.find_elements(*self.pindao)[num].click()
		else:
			print '输入类型有误'

	def getLastItemText(self):
		"""
		获取最后一个频道的名称
		:return: str, 最后一个频道的名称
		"""
		text = self.find_elements(*self.pindao)[self.getLenth()].text
		return text
