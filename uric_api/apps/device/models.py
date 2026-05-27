from django.db import models
from uric_api.apps.base.models import BaseModel

class DeviceAttrModel(BaseModel):
	attr_status = models.BooleanField(verbose_name="设备状态")
	attr_name = models.CharField(max_length = 100,verbose_name="属性名称")
	attr_value = models.CharField(max_length = 100,verbose_name="属性值")
	p_attr = models.CharField(max_length = 100, verbose_name="父属性")
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_device_attr'
		ordering = ['-created_time']

		

class DeviceModel(BaseModel):
	device_attr = models.ForeignKey(DeviceAttrModel, on_delete = models.CASCADE)
	device_name = models.CharField(max_length = 100)
	device_status = models.CharField(max_length = 100)
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_devices'
		ordering = ['-created_time']