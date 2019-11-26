import markdown
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags

from userapp.models import User


# Create your models here.
class Category(models.Model):
	"""
	分类表
	"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '类别'
		verbose_name_plural = verbose_name  # 复数形式


class Tag(models.Model):
	"""
	标签表
	"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = verbose_name


class Article(models.Model):
	"""
	文章表
	"""
	# 文章标题
	title = models.CharField('标题', max_length=70)

	# 文章正文，TextField
	body = models.TextField('正文')

	# 文章创建时间和最后一次的修改时间
	created_time = models.DateTimeField('创建时间', default=timezone.now)
	modified_time = models.DateTimeField('修改时间')

	# 文章摘要,blank-允许为空
	abstract = models.CharField('摘要', max_length=200, blank=True)

	# 分类为一对多，用外键，分类删除，该分类下的文章都删除,级联删除；
	# 标签为多对多
	category = models.ForeignKey(Category, verbose_name='类别', on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

	# 文章作者，从django自带的用户管理导入的
	# 也是一对多的关系
	# 这里不设定related_name,序列化的时候，调用PrimaryKeyRelatedField，必须用模型名加set，即article_set
	# 不然会报AttributeError: 'User' object has no attribute 'blogapp_set'
	author = models.ForeignKey(User, related_name='article_list', verbose_name='作者', on_delete=models.CASCADE)

	# 新增views字段，记录阅读量
	views = models.PositiveIntegerField(default=0, editable=False)

	def save(self, *args, **kwargs):
		"""
		父类函数，保存数据到数据库
		:param args:
		:param kwargs:
		:return:
		"""
		self.modified_time = timezone.now()

		# 首先实例化一个markdown对象，渲染博客正文
		# 摘要不需要目录，去掉目录扩展
		md = markdown.Markdown(extension=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
		])
		# 现将markdown文本渲染为html文本
		# strip_tags去掉html文本的全部html标签
		# 从文本摘取前54个字符作为摘要
		self.abstract = strip_tags(md.convert(self.body))[:54]

		super(self, Article).save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = verbose_name

		# 指定排序属性
		ordering = ['-created_time']
