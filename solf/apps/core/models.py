from django.db import models
from model_utils.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel, TimeStampedModel):
    name = models.CharField(max_length=30, verbose_name='Name')
    parent = TreeForeignKey('self',
                            verbose_name='Parent Category',
                            related_name='sub_categories',
                            on_delete=models.DO_NOTHING,
                            blank=True,
                            null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
