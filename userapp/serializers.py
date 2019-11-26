# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 0026 13:25
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: serializers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me

from rest_framework import serializers

from blogapp.models import Article
from common.commonFun import entryMd5
from userapp.models import User


# 用于注册的时候返回json数据
class UserRegisterSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		validated_data['password'] = entryMd5(validated_data['password'])
		return super(UserRegisterSerializer, self).create(validated_data)

	class Meta:
		exclude = []  # 序列化中排除的字段
		model = User
		fields = ('id', 'user_name', 'password', 'nick_name', 'user_email')  # 显示指定某个model中需要序列化的字段


class UserSerializer(serializers.ModelSerializer):
	article_list = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
	class Meta:
		exclude = []
		model = User
		fields = ('id', 'user_name', 'article_list')
