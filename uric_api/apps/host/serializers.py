from rest_framework import serializers
from .models import HostCategory, Host

class HostCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = HostCategory
		fields = ['id','name']
		
class HostSerializer(serializers.ModelSerializer):
	category_name = serializers.CharField(source='category.name', read_only=True)
	password = serializers.CharField(max_length=32, write_only=True, label="登录密码")
	
	class Meta:
		model = Host
		fields = ['id', 'category', 'category_name', 'name', 'ip_addr', 'port', 'description', 'username', 'password']
		
	def validate(self, attrs):
		ip_addr = attrs.get('ip_addr')
		port = attrs.get('port')
		username = attrs.get('username')
		password = attrs.get('password')
		return attrs
		
	def create(self, validated_data):
		ip_addr = validated_data.get('ip_addr')
		port = validated_data.get('port')
		username = validated_data.get('username')
		password = validated_data.pop('password' , None)
			
		instance = Host.objects.create(**validated_data)
		return instance