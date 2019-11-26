# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 0026 16:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: commonFun.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import hashlib


def entryMd5(data):
	"""
	32位MD5加密数据
	:param data 传入的数据:
	:return 返回加密后的MD5码:
	"""
	entry = hashlib.md5()
	entry.update(data.encode('utf-8'))
	return entry.hexdigest()
