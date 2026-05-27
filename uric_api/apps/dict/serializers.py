from rest_framework import serializers
from .models import DictTypeModel, DictDataModel





class DictDataSerializer(serializers.ModelSerializer):
    """
        字典项目序列化类
    """
    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.value = validated_data.get('value', instance.value)
        instance.status = validated_data.get('status', instance.status)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.save()
        return instance

    class Meta:
        model = DictDataModel
        fields = '__all__'
        
        
class DictTypeSerializer(serializers.ModelSerializer):
    """
        字典类型序列化类
    """
    dict_items = DictDataSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.type_name = validated_data.get('type_name', instance.type_name)
        instance.type_code = validated_data.get('type_code', instance.type_code)
        instance.status = validated_data.get('status', instance.status)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.save()
        return instance

    class Meta:
        model = DictTypeModel
        fields = '__all__'
        
