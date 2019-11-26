# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 0026 13:26
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: serializers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from rest_framework import serializers

from blogapp.models import Article


class ArticleSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.nick_name')  # 只读

	class Meta:
		exclude = []
		model = Article
		fields = (
		'id', 'title', 'body', 'created_time', 'modified_time', 'abstract', 'category', 'tags', 'author', 'views')
