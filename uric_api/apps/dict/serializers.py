from rest_framework import serializers
from .models import DictTypeModel, DictDataModel


class DictTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictTypeModel
        fields = '__all__'


class DictDataSerializer(serializers.ModelSerializer):
    # 前端使用 item_value 字段，映射到数据库的 label 字段
    item_value = serializers.CharField(source='value', required=True)
    item_name = serializers.CharField(source='label', required=True)
    class Meta:
        
        model = DictDataModel
        fields = ['id', 'is_show', 'orders', 'is_deleted', 'created_time',
                  'updated_time', 'delete_time', 'remark', 'dict_type',
                  'item_value', 'item_name', 'status']
