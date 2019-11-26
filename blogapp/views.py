from rest_framework import viewsets

from blogapp.serializers import *
from userapp.models import User
from userapp.permissions import IsOwnerOrReadOnly


# Create your views here.
# 用于博客的增删改查，除了查看，其他都需要权限
class BlogViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = (IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		print(self.request.user)
		serializer.save(author=User.objects.get(id=self.request.session.get('user_id')))
