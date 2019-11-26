# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from userapp.serializers import *


# 用于登录
class UserLoginAPIView(APIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

	def post(self, request, format=None):
		data = request.data
		user_name = data.get('user_name')
		password = entryMd5(data.get('password'))
		user = User.objects.get(user_name__exact=user_name)
		if user.password == password:
			serializer = UserSerializer(user)
			# 记忆已登录用户
			self.request.session['user_id'] = user.id
			return Response(serializer.data, status=HTTP_200_OK)
		return Response('密码错误', HTTP_400_BAD_REQUEST)


# 用于注册
class UserRegisterAPIView(APIView):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer
	permission_classes = (AllowAny,)

	def post(self, request, format=None):
		data = request.data
		user_name = data.get('user_name')
		if User.objects.filter(user_name__exact=user_name):
			return Response('用户名已存在', HTTP_400_BAD_REQUEST)
		serializer = UserRegisterSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			# print(serializer.validated_data)
			serializer.save()
			return Response("注册成功", status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
