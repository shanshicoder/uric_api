from django.db import models

# Create your models here.
class BaseModel(models.Model):
	is_show = models.BooleanField(default=True , verbose_name="是否显示")
	orders = models.IntegerField(default=1 , verbose_name="排序")
	is_deleted = models.BooleanField(default=False , verbose_name="是否删除")
	created_time = models.DateTimeField(auto_now_add=True , verbose_name="添加时间")
	updated_time = models.DateTimeField(auto_now=True , verbose_name="修改时间")
	delete_time = models.DateTimeField(auto_now=True , verbose_name="删除时间")
	remark = models.TextField(null=True , blank=True , default="" , verbose_name="备注")

	class Meta:
		abstract = True

	def __str__(self):
		return self.name


class DictTypeModel(BaseModel):
	# 字典类型名称
	type_name = models.CharField(max_length=100, verbose_name="类型名称")
	# 字典类型编码，唯一
	type_code = models.CharField(max_length=100, unique=True, verbose_name="类型编码")
	# 状态：启用/禁用
	status = models.BooleanField(verbose_name="状态")

	def __str__(self):
		return self.type_name

	class Meta:
		db_table = 'uric_dict_type'
		ordering = ['-created_time']
		verbose_name = '字典类型'
		verbose_name_plural = verbose_name
		app_label = 'dict'


class DictDataModel(BaseModel):

	dict_type = models.ForeignKey(DictTypeModel, on_delete=models.CASCADE,related_name="dict_items", verbose_name="字典类型")
	label = models.CharField(max_length=100, verbose_name="显示标签")
	value = models.CharField(max_length=100, verbose_name="字典值")

	def __str__(self):
		return f"{self.label} ({self.value})"

	class Meta:
		db_table = 'uric_dict_data'
		ordering = ['orders', '-created_time']
		verbose_name = '字典数据'
		verbose_name_plural = verbose_name
		app_label = 'dict'