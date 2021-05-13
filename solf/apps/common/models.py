import datetime

from django.db import models

from model_utils.models import TimeStampedModel


class WeekdayTimeMixin(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    WEEK_DAYS = (
        (1, MONDAY),
        (2, TUESDAY),
        (3, WEDNESDAY),
        (4, THURSDAY),
        (5, FRIDAY),
        (6, SATURDAY),
        (7, SUNDAY)
    )
    weekday = models.PositiveSmallIntegerField(
        verbose_name='Weekday',
        choices=WEEK_DAYS
    )
    start_time = models.TimeField(
        verbose_name='Start time',
        default=datetime.time(9, 0)
    )
    end_time = models.TimeField(
        verbose_name='End time',
        default=datetime.time(18, 0)
    )

    class Meta:
        abstract = True


class GeoLocationMixin(models.Model):
    latitude = models.FloatField(
        verbose_name='Latitude',
        null=True,
    )
    longitude = models.FloatField(
        verbose_name='Longitude',
        null=True
    )

    class Meta:
        abstract = True


class LocationMixin(models.Model):
    address = models.CharField(
        verbose_name='Address',
        max_length=200
    )

    class Meta:
        abstract = True


class ContactsMixin(models.Model):
    phone = models.CharField(
        verbose_name='Phone',
        max_length=20
    )
    website = models.URLField(
        verbose_name='Website',
        max_length=30,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=30,
        blank=True
    )

    class Meta:
        abstract = True


class City(TimeStampedModel, GeoLocationMixin):
    name = models.CharField(
        verbose_name='City name',
        max_length=30
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(
        verbose_name='Active?',
        default=True
    )

    class Meta:
        abstract = True
