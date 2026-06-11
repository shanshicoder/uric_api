from django.db import models

# Create your models here.
class FileModel(models.Model):
    file_path = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True,db_comment='文件路径')
    filename = models.CharField(max_length=255,blank=True,null=True,db_comment="文件名")
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,db_comment='上传时间')

    def __str__(self):
        return self.filename
