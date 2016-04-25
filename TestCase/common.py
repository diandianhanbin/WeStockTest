# ecoding=utf-8
import os
__author__ = "Sven_Weng"

add = os.getcwd().split('/')
add.pop(len(add)-1)

add = '/'.join(add)+'/Data/'
print add


class common:
	def __init__(self):
		pass

	def get_address(self):
		add = os.getcwd().split('/')
		add.pop(len(add) - 1)
		add = '/'.join(add) + '/Data/data.json'
		return add