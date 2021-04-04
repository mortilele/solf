from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from solf.apps.common.models import LocationMixin, ContactsMixin, City, GeoLocationMixin


class Business(TimeStampedModel):
    name = models.CharField(
        max_length=200
    )

    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Business'


class Amenity(TimeStampedModel):
    name = models.CharField(
        verbose_name='Amenity name',
        max_length=20,
    )

    class Meta:
        verbose_name = 'Fitness amenity'
        verbose_name_plural = 'Fitness amenities'


class Fitness(TimeStampedModel, LocationMixin, GeoLocationMixin, ContactsMixin):
    name = models.CharField(
        verbose_name='Fitness name',
        max_length=100,
    )
    description = models.TextField(
        verbose_name='Short description',
        blank=True,
        null=True
    )
    business = models.ForeignKey(
        Business,
        verbose_name='Business',
        on_delete=models.CASCADE,
        related_name='fitnesses',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    amenities = models.ManyToManyField(
        Amenity,
        verbose_name='Fitness Amenities',
        related_name='fitnesses',
        blank=True
    )

    class Meta:
        verbose_name = 'Fitness'
        verbose_name_plural = 'Fitnesses'
