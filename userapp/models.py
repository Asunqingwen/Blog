from django.db import models


# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=20, null=False)
	password = models.CharField(max_length=32, null=False)
	nick_name = models.CharField(max_length=10, null=False)
	user_email = models.EmailField(max_length=20, null=False)

	def __str__(self):
		return self.user_name

	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name  # 复数形式
