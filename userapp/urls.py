# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 0026 14:51
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: urls.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from django.urls import re_path

from userapp import views

urlpatterns = [
	re_path(r'^register', views.UserRegisterAPIView.as_view()),
	re_path(r'^login', views.UserLoginAPIView.as_view()),
]
