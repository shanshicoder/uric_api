from django.db import models

class BaseModel(models.Model):
    is_show = models.BooleanField(default=True, verbose_name="是否显示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    delete_time = models.DateTimeField(auto_now=True, verbose_name="删除时间")
    remark = models.TextField(null=True, blank=True, default="", verbose_name="备注")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name