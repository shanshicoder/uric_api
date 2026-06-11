from django.db import models
from uric_api.apps.base.models import BaseModel

class DeviceAttrModel(BaseModel):

	attr_status = models.BooleanField(verbose_name="设备状态", default=True)
	attr_name = models.CharField(max_length = 100,verbose_name="属性名称")
	attr_value = models.CharField(max_length = 100,verbose_name="属性值")
	p_attr = models.IntegerField(default=0)
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_device_attr'
		ordering = ['-created_time']

		

class DeviceModel(BaseModel):
	device_name = models.CharField(max_length = 100,db_comment='设备名',null=True, blank=True,)
	device_attr = models.CharField(max_length = 100,db_comment='设备属性',null=True, blank=True,)
	buy_in = models.DateField(db_comment='采购日期',null=True, blank=True,)
	device_code = models.CharField(max_length=20,db_comment='设备编号',null=True, blank=True,)
	device_status = models.CharField(max_length = 100,db_comment='设备状态',null=True, blank=True,)
	sn_pn = models.CharField(max_length=50, db_comment='SN/PN',null=True, blank=True,)
	device_pic = models.CharField(max_length=200,db_comment='设备图片',null=True, blank=True,)
	device_type = models.CharField(max_length=20,db_comment='设备类型',null=True, blank=True,)
	
	class Meta:
		# 元选项：定义表名、排序、复合索引等
		db_table = 'uric_devices'
		ordering = ['-created_time']

class DeviceRecordModel(BaseModel):
	user = models.CharField(max_length=20,db_comment='领用人')
	opt = models.CharField(max_length=20,db_comment='操作')
	class Meta:
		db_table = 'uric_device_record'
		ordering = ['-created_time']
