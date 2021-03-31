from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
