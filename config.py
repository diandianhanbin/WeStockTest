# ecoding=utf-8
# Author: Sven_Weng | 翁彦彬
# Email: diandianhanbin@gmail.com
from selenium.webdriver.common.by import By

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
	'data_url': '/Users/SvenWeng/PycharmProjects/WeStock/Data/data.json',
	'view_title': (By.CLASS_NAME, 'android.widget.TextView'),
	'ensure': (By.NAME, u'确定'),
	'cancle': (By.NAME, u'取消'),
}

CAIXUN = {
	'tuijian': (By.NAME, u'推荐'),
	'gupiao': (By.NAME, u'股票'),
	'jijin': (By.NAME, u'基金'),
	'zhaiquan': (By.NAME, u'债券'),
	'xinsanban': (By.NAME, u'新三板'),
	'zixunneirong': (By.ID, 'com.weizq:id/new_title'),  # 财讯记录列表,用find_elements调用
	'imgurl': '/Users/SvenWeng/PycharmProjects/WeStock/img/caixun/',
	'title': [
		['tuijian', 'tuijianneirong'],
		['gupiao', 'gupiaoneirong'],
		['jijin', 'jijinneirong'],
		['zhaiquan', 'zhaiquanneirong'],
		['xinsanban', 'xinsanbanneirong']
	],
	'jiahao': (By.CLASS_NAME, 'android.widget.ImageView'),
	'pindao': (By.ID, 'com.weizq:id/text_item'),
}

HANGQING = {
	# ----------行情页面-------------
	'edit_select': (By.CLASS_NAME, 'android.widget.ImageView'),  # index[0]
	'find_stock': (By.CLASS_NAME, 'android.widget.ImageView'),  # index[1]
	'zixuan': (By.NAME, u'自选'),
	'hushen': (By.NAME, u'沪深'),
	'ganggu': (By.NAME, u'港股'),
	'gengduo': (By.NAME, u'更多'),
	'mingchendaima': (By.ID, 'com.weizq:id/tztStockCodeName_title'),  # 名称代码
	'zuixinjia': (By.ID, 'com.weizq:id/tztCodePrice_title'),  # 最新价
	'zhangdiefu': (By.ID, 'com.weizq:id/tztTextWillchange_title'),  # 涨跌幅
	'stock': {
		'info': (By.ID, 'com.weizq:id/tztStockCodeNameLayout'),  # 股票
		'name': (By.ID, 'com.weizq:id/tztStockCodeName'),  # 股票名称
		'num': (By.ID, 'com.weizq:id/tztSotckCode'),  # 股票代码
	},
	'price': (By.ID, 'com.weizq:id/tztCodePrice'),  # 股票价格
	'newprice': (By.ID, 'com.weizq:id/tztCodePrice_title'),  # 最新价
	'newzhangdiefu': (By.ID, 'com.weizq:id/tztTextWillchange'),  # 涨跌幅下面的指标

	# ----------编辑自选页面-------
	'delete': (By.ID, 'com.weizq:id/tzt_del_userstock_icon'),  # 删除自选
	'settop': (By.ID, 'com.weizq:id/tzt_zhiding_userstock_icon'),  # 置顶
	'move': (By.ID, 'com.weizq:id/tzt_move_userstock_icon'),  # 拖动
	'stock_name': (By.ID, 'com.weizq:id/tzt_userstock_text'),  # 股票名称
	'stock_num': (By.ID, 'com.weizq:id/tzt_userstock_text2'),  # 股票代码
	'move_title': (By.NAME, u'拖动'),  # 拖动 标题

	# ----------查找自选页面-------
	'input': (By.ID, 'com.weizq:id/tz_searchstock_edit'),  # 搜索框
	'stock_name_search': (By.ID, 'com.weizq:id/tzt_querystock_list_col1'),  # 搜索结果的股票名称
	'stock_num_search': (By.ID, 'com.weizq:id/tzt_querystock_list_col4'),  # 搜索结果的股票代码
	'addordel_stock': (By.ID, 'com.weizq:id/tzt_querystock_list_col3'),  # 添加或删除自选
	'clean_history': (By.ID, 'com.weizq:id/tzt_querystock_list_col5'),  # 清除搜索记录&股票代码不存在
}
