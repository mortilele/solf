import datetime

from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class WeekdayTimeMixin(models.Model):
    MONDAY = 'Понедельник'
    TUESDAY = 'Вторник'
    WEDNESDAY = 'Среда'
    THURSDAY = 'Четверг'
    FRIDAY = 'Пятница'
    SATURDAY = 'Суббота'
    SUNDAY = 'Воскресенье'

    WEEK_DAYS = (
        (1, MONDAY),
        (2, TUESDAY),
        (3, WEDNESDAY),
        (4, THURSDAY),
        (5, FRIDAY),
        (6, SATURDAY),
        (7, SUNDAY)
    )
    weekday = models.PositiveSmallIntegerField(verbose_name='Weekday',
                                               choices=WEEK_DAYS)
    start_time = models.TimeField(verbose_name='Start time', default=datetime.time(9, 0))
    end_time = models.TimeField(verbose_name='End time', default=datetime.time(18, 0))

    class Meta:
        abstract = True


class GeoLocationMixin(models.Model):
    latitude = models.FloatField(null=True, verbose_name='Latitude')
    longitude = models.FloatField(null=True, verbose_name='Longitude')

    class Meta:
        abstract = True


class LocationMixin(models.Model):
    address = models.CharField(max_length=200, verbose_name='Address')

    class Meta:
        abstract = True


class ContactsMixin(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Phone')
    website = models.URLField(max_length=30, blank=True, verbose_name='Website')
    email = models.EmailField(max_length=30, blank=True, verbose_name='E-mail')

    class Meta:
        abstract = True


class City(TimeStampedModel, GeoLocationMixin):
    name = models.CharField(max_length=30, verbose_name='City name')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
