from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from solf.apps.business.models import Fitness
from solf.apps.common.models import WeekdayTimeMixin
from solf.apps.core.models import Category


class Class(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name='Class name')
    fitness = models.ForeignKey(Fitness,
                                on_delete=models.CASCADE,
                                related_name='classes',
                                verbose_name='Fitness')
    description = models.TextField(verbose_name='About class', blank=True, null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 related_name='classes',
                                 verbose_name='Class Category')
    max_spots = models.PositiveSmallIntegerField(verbose_name='Maximum available spots')

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class ClassSchedule(TimeStampedModel, WeekdayTimeMixin):
    class_template = models.ForeignKey(Class,
                                       on_delete=models.CASCADE,
                                       related_name='schedule',
                                       verbose_name='Class')
    max_spots = models.PositiveSmallIntegerField(verbose_name='Maximum available spots')

    class Meta:
        verbose_name = 'Class Schedule'
        verbose_name_plural = 'Classes Schedule'


class ClassScheduleLogs(TimeStampedModel):
    schedule = models.ForeignKey(ClassSchedule,
                                 on_delete=models.DO_NOTHING,
                                 verbose_name='Schedule',
                                 related_name='logs')

    class Meta:
        verbose_name = 'Class Schedule Logs'
        verbose_name_plural = 'Classes Schedule Logs'
