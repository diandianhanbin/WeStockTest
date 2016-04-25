# ecoding=utf-8
from selenium.webdriver.common.by import By
__author__ = "Sven_Weng"

CONNECT = {
	'platformName': 'Android',
	'platformVersion': '4.4.4',
	'deviceName': '5136b01e',
	'appPackage': 'com.weizq',
	'appActivity': 'com.zztzt.android.simple.app.MainActivity',
	"baseUrl": "http://127.0.0.1:4723/wd/hub"
}

COMMON = {
	'native_caixun': (By.NAME, u'财讯'),
	'native_hangqing': (By.NAME, u'行情'),
	'native_faxian': (By.NAME, u'发现'),
	'native_wo': (By.NAME, u'我'),
	'data_url': '/Users/SvenWeng/PycharmProjects/WeStock/Data/data.json'
}

CAIXUN = {
	'tuijian': (By.NAME, u'推荐'),
	'gupiao': (By.NAME, u'股票'),
	'jijin': (By.NAME, u'基金'),
	'zhaiquan': (By.NAME, u'债券'),
	'xinsanban': (By.NAME, u'新三板'),
	'zixunneirong': (By.ID, 'com.weizq:id/new_title'),  # 财讯记录列表,用find_elements调用
	'imgurl': '/Users/SvenWeng/PycharmProjects/WeStock/img/caixun/',
	'back': (By.ID, 'com.weizq:id/back_iv')
}