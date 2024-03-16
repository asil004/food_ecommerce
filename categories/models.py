from django.db import models
from mptt.models import TreeForeignKey,MPTTModel
from base.models import TimeStampModel


class Category(MPTTModel,TimeStampModel):
    category_name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='cate_product')

    @classmethod
    def publish(cls):
        return cls.objects.all()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.category_name
