from rest_framework import serializers
from .models import DeviceModel, DeviceAttrModel

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeviceModel
		fields = '__all__'


class DeviceAttrSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeviceAttrModel
		fields = '__all__'
