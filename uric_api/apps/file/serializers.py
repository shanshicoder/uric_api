import os

from rest_framework import serializers
from .models import FileModel

class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = FileModel
        fields = ['id', 'file_path', 'filename', 'file_url', 'uploaded_at']
        read_only_fields = ['filename']

    def get_file_url(self, obj):
        if obj.file_path:
            return obj.file_path
        return None

    def validate_file(self, value):
        """
            文件校验：校验大小和格式
        """

        max_size = 1024 * 1024 * 10
        if value.size > max_size:
            raise serializers.ValidationError('文件大小超出10MB')

        valid_ext = ['.jpg', '.jpeg', '.png','.pdf', '.xlsx','.docx','.txt']
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in valid_ext:
            raise serializers.ValidationError('文件格式不支持')
        return value

    def create(self, validated_data):
        # 在保存时，自动将文件的原始名称提取出来存入数据库
        file_obj = validated_data['file']
        validated_data['filename'] = file_obj.name
        return super().create(validated_data)