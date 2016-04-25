# ecoding=utf-8
import time
import config
from selenium.webdriver.common.by import By
from View.BaseView import AppUI
__author__ = "Sven_Weng"


class Caixun(AppUI):

	# ----------------------财讯所有数据--------------------------
	native_caixun = config.COMMON['native_caixun']
	native_hangqing = config.COMMON['native_hangqing']
	native_faxian = config.COMMON['native_faxian']
	native_wo = config.COMMON['native_wo']

	tuijian = config.CAIXUN['tuijian']
	gupiao = config.CAIXUN['gupiao']
	jijin = config.CAIXUN['jijin']
	zhaiquan = config.CAIXUN['zhaiquan']
	xinsanban = config.CAIXUN['xinsanban']
	neirong = config.CAIXUN['zixunneirong']

	img_url = config.CAIXUN['imgurl']

	back = config.CAIXUN['back']

	# ----------------------------------------------------------

	# ---------------------执行方法------------------------------

	def clickCaixun(self):
		self.find_element(*self.native_caixun).click()
		time.sleep(2)

	def clickHangqing(self):
		self.find_element(*self.native_hangqing).click()
		time.sleep(2)

	def clickFaxian(self):
		self.find_element(*self.native_faxian).click()

	def clickWo(self):
		self.find_element(*self.native_wo).click()

	def get_screen(self, name):
		self.getScreenshot(name, self.img_url)

	def clickTuijian(self):
		self.find_element(*self.tuijian).click()

	def clickGupiao(self):
		self.find_element(*self.gupiao).click()

	def clickJijin(self):
		self.find_element(*self.jijin).click()

	def clickZhaiquan(self):
		self.find_element(*self.zhaiquan).click()

	def clickXinsanban(self):
		self.find_element(*self.xinsanban).click()

	def clickNeirong(self):
		self.find_elements(*self.neirong)[0].click()

	def goBack(self):
		self.find_element(*self.back).click()
