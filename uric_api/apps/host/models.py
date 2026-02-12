from django.db import models

from users.models import User


# Create your models here.
class BaseModel(models.Model):
	name = models.CharField(max_length=500,default='',null=True,blank=True, verbose_name="名称/标题")
	is_show = models.BooleanField(default=True, verbose_name="是否显示")
	orders = models.IntegerField(default=1,verbose_name="排序")
	is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
	updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
	description = models.TextField(null=True, blank=True, default="", verbose_name="描述信息")
	
	class Meta:
		abstract = True
		
	def __str__(self):
		return self.name

class HostCategory(BaseModel):
	
	class Meta:
		db_table = 'uric_host_category'
		verbose_name = "主机类别"
		verbose_name_plural = verbose_name
	
class Host(BaseModel):
	category = models.ForeignKey("HostCategory", on_delete=models.DO_NOTHING, verbose_name="主机类别",related_name='hc',null=True, blank=True)
	ip_addr = models.CharField(blank=True,null=True,max_length=500,verbose_name="连接地址")
	port = models.IntegerField(verbose_name="端口")
	username = models.CharField(max_length=50, verbose_name="登录用户")
	users = models.ManyToManyField(User)
	password = models.CharField(max_length=32, verbose_name="登录用户")
	class Meta:
		db_table = 'uric_host'
		verbose_name = "主机信息"
		verbose_name_plural = verbose_name
		
	def __str__(self):
		return f"{self.name}@{self.ip_addr}:{self.port}"