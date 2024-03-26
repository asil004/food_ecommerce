from django.db import models
from mptt.models import TreeForeignKey, MPTTModel
from base.models import TimeStampModel
from audioop import reverse

class Category(MPTTModel, TimeStampModel):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True,null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='cate_product')

    @classmethod
    def publish(cls):
        return cls.objects.all()

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category', kwargs={self.slug})
