from rest_framework import serializers
from .models import DeviceModel, DeviceAttrModel, DeviceCateModel

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeviceModel
		fields = '__all__'


class DeviceAttrSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeviceAttrModel
		fields = '__all__'
		

class DeviceCateSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeviceCateModel
		fields = '__all__'

		