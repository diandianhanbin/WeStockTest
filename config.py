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

	'imgurl': '/Users/SvenWeng/PycharmProjects/WeStock/img/hangqing/',
	'imgurl_zixuan': '/Users/SvenWeng/PycharmProjects/WeStock/img/hangqing/zixuan/',
	'imgurl_hushen': '/Users/SvenWeng/PycharmProjects/WeStock/img/hangqing/hushen/',
	'imgurl_ganggu': '/Users/SvenWeng/PycharmProjects/WeStock/img/hangqing/ganggu/',
	'imgurl_more': '/Users/SvenWeng/PycharmProjects/WeStock/img/hangqing/more/',

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

	# ----------自选详情页面-------
	'zixuan_stock_detail': (By.ID, 'com.weizq:id/zixuan_btn'),  # 添加删除自选
	'buy_detail': (By.ID, 'com.weizq:id/mairu_btn'),  # 买入
	'sale_detail': (By.ID, 'com.weizq:id/maichu_btn'),  # 卖出
	'share_detail': (By.ID, 'com.weizq:id/share_btn'),  # 分享
	'fenshi': (By.NAME, u'分时'),
	'rik': (By.NAME, u'日K'),
	'zhouk': (By.NAME, u'周K'),
	'yuek': (By.NAME, u'月K'),

	# ---------沪深页面-----------------
	'xingurili': (By.NAME, u'新股日历'),
	'shangzhengzhishu': (By.NAME, u'上证指数'),
	'shengzhengchengzhi': (By.NAME, u'深圳成指'),
	'chuangyebanzhi': (By.NAME, u'创业板指'),
	'getmore': (By.ID, 'com.weizq:id/tztMoreImage'),
	'remenhangye': (By.NAME, u'热门行业'),
	'zhangfubang': (By.NAME, u'涨幅榜'),
	'diefubang': (By.NAME, u'跌幅榜'),
	'huanshoubang': (By.NAME, u'换手榜'),
	'zhenfubang': (By.NAME, u'振幅榜'),

	# ---------港股页面-----------------
	'ganggutongzhangfubang': (By.NAME, u'港股通涨幅榜'),
	'ganggutongdiefubang': (By.NAME, u'港股通跌幅榜'),
	'zhubangzhangfubang': (By.NAME, u'主板涨幅榜'),
	'zhubangdiefubang': (By.NAME, u'主板跌幅榜'),
	'remenahgu': (By.NAME, u'热门AH股'),
	'hongchougu': (By.NAME, u'红筹股'),
	'lanchougu': (By.NAME, u'蓝筹股'),

	# ---------更多页面-----------------

}
