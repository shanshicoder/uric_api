from django.db import models


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
	
	
class DeviceCateModel(BaseModel):
	# 字段定义
	device_cate = models.CharField(max_length = 100, verbose_name="设备类别")
	device_status = models.BooleanField(verbose_name="设备状态")
	def __str__(self):
		# 定义在后台管理或打印对象时显示的字符串
		return f"{self.field_name}"
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_device_cate'
		ordering = ['-created_time']


class DeviceAttrModel(BaseModel):
	device_id = models.CharField(max_length = 100)
	device_brand = models.CharField(max_length=100)
	device_cpu = models.CharField(max_length = 100)
	device_memory = models.CharField(max_length = 100)
	device_disk = models.CharField(max_length = 100)
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_device_attr'
		ordering = ['-created_time']
		

class DeviceModel(BaseModel):
	device_cate = models.ForeignKey(DeviceCateModel, on_delete = models.CASCADE)
	device_attr = models.ForeignKey(DeviceAttrModel, on_delete = models.CASCADE)
	device_name = models.CharField(max_length = 100)
	device_status = models.CharField(max_length = 100)
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_devices'
		ordering = ['-created_time']