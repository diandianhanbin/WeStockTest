# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : diandianhanbin@gmail.com

import config
from View.BaseView import AppUI


class MobileLogin(AppUI):
	# ------------登录页面-------------
	username_edit = config.MOBILELOGIN['username_edit']
	password_edit = config.MOBILELOGIN['password_edit']
	login_btn = config.MOBILELOGIN['login_btn']


	# ------------执行方法-------------
	def sendUserName(self, val):
		"""
		在用户名输入框上输入用户名
		:param val:用户名
		:return:None
		"""
		self.find_element(*self.username_edit).send_keys(val)

	def sendPassWord(self, val):
		"""
		在密码输入框上输入密码
		:param val: 密码
		:return: None
		"""
		self.find_element(*self.password_edit).send_keys(val)

	def clickLoginBtn(self):
		"""
		点击登录按钮
		:return:None
		"""
		self.find_element(*self.login_btn).click()