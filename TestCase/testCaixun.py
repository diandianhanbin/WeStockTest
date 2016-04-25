# ecoding=utf-8
import unittest
import json
import config
from View.Caixun import Caixun
from View.BaseTestCase import AppTestCase
__author__ = "Sven_Weng"


class CaixunTest(AppTestCase, Caixun):

	def testClickTitle(self):
		self.clickCaixun()
		self.clickTuijian()
		self.get_screen('tuijian')
		self.clickNeirong()
		self.get_screen('tuijianneirong')
		self.goBack()
		self.clickGupiao()
		self.get_screen('gupiao')
		self.clickNeirong()
		self.get_screen('gupiaoneirong')
		self.goBack()
		self.clickJijin()
		self.get_screen('jijin')
		self.clickNeirong()
		self.get_screen('jijinneirong')
		self.goBack()
		self.clickZhaiquan()
		self.get_screen('zhaiquan')
		self.clickNeirong()
		self.get_screen('zhaiquanneirong')
		self.goBack()
		self.clickXinsanban()
		self.get_screen('xinsanban')
		self.clickNeirong()
		self.get_screen('xinsanbanneirong')


if __name__ == '__main__':
	unittest.main(verbosity=2)
