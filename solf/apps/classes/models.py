from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.functional import cached_property
from djmoney.models.fields import MoneyField
from imagekit.models import ProcessedImageField, ImageSpecField
from model_utils.models import TimeStampedModel

from solf.apps.business.models import Fitness
from solf.apps.common.models import WeekdayTimeMixin, IsActiveMixin
from solf.apps.common.utils import image_specs
from solf.apps.common.utils.file_extension_validators import IMAGE_ALLOWED_EXTENSIONS
from solf.apps.core.models import Category
from solf.apps.users.models import UserPass

"""
================================================
=         How is it supposed to work?          =
================================================

- Current Active classes relates to ClassSchedule
- Passed classes will be transferred to ClassLog

- Upcoming User entries relates to schedule
- Passed to logs
- For Dashboard analytics will be implemented mapper for schedule, logs
"""


class ClassPriceMixin(models.Model):
    one_entry_price = MoneyField(
        verbose_name='One Entry Price',
        max_digits=10,
        decimal_places=2,
        default_currency='KZT',
        default=0.00
    )

    class Meta:
        abstract = True


class ClassEntryTypeMixin(models.Model):
    class EntryType(models.TextChoices):
        BOOKING = 'BOOKING', 'In app booking'
        CALLING = 'CALLING', 'Phone call'

    entry_type = models.CharField(
        verbose_name='Entry Type',
        choices=EntryType.choices,
        max_length=20,
        default=EntryType.BOOKING.value
    )

    class Meta:
        abstract = True


class Class(
    TimeStampedModel,
    ClassEntryTypeMixin,
    ClassPriceMixin,
    IsActiveMixin
):
    def class_image_path(instance, filename):
        import uuid
        extension = filename.split(".")[-1]
        return f"classes/{uuid.uuid4()}.{extension}"

    name = models.CharField(
        verbose_name='Class name',
        max_length=50,
    )
    fitness = models.ForeignKey(
        Fitness,
        verbose_name='Fitness',
        on_delete=models.CASCADE,
        related_name='classes',
    )
    description = models.TextField(
        verbose_name='About class',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Class Category',
        on_delete=models.DO_NOTHING,
        related_name='classes',
    )
    max_spots = models.PositiveSmallIntegerField(
        verbose_name='Maximum available spots'
    )
    image = ProcessedImageField(
        verbose_name='Class Image',
        blank=True,
        null=True,
        upload_to=class_image_path,
        spec=image_specs.HDSpec,
        validators=[
            FileExtensionValidator(
                allowed_extensions=IMAGE_ALLOWED_EXTENSIONS)
        ]
    )
    thumbnail = ImageSpecField(
        source='image',
        spec=image_specs.ThumbnailSpec
    )

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f'{self.name} - {self.fitness}'


class ClassMixin(models.Model):
    class_template = models.ForeignKey(
        Class,
        verbose_name='Class',
        on_delete=models.CASCADE,
        related_name='%(class)s'
    )
    max_spots = models.PositiveSmallIntegerField(
        verbose_name='Maximum available spots'
    )

    class Meta:
        abstract = True


class ClassSchedule(
    ClassMixin,
    TimeStampedModel,
    WeekdayTimeMixin,
    IsActiveMixin
):
    class Meta:
        verbose_name = 'Class Schedule'
        verbose_name_plural = 'Classes Schedule'


class ClassLog(
    ClassMixin,
    ClassEntryTypeMixin,
    ClassPriceMixin,
    TimeStampedModel,
    WeekdayTimeMixin
):
    """
    Passed classes warehouse
    """
    schedule = models.ForeignKey(
        ClassSchedule,
        verbose_name='Schedule',
        on_delete=models.DO_NOTHING,
        related_name='logs'
    )

    class Meta:
        verbose_name = 'Class Logs'
        verbose_name_plural = 'Classes Logs'


class ClassUserEntry(TimeStampedModel):
    class EntryStatus(models.TextChoices):
        WAITING = 'WAITING', 'Waiting'
        CANCELED_BY_USER = 'CANCELED_BY_USER', 'Canceled by user'
        CANCELED_BY_MODERATOR = 'CANCELED_BY_MODERATOR', 'Canceled by moderator'
        MISSED = 'MISSED', 'Missed'
        APPROVED = 'APPROVED', 'Approved successfully'

    status = models.CharField(
        verbose_name='Entry Type',
        choices=EntryStatus.choices,
        max_length=30,
        default=EntryStatus.WAITING.value
    )
    schedule = models.ForeignKey(
        ClassSchedule,
        verbose_name='Schedule',
        on_delete=models.DO_NOTHING,
        related_name='entries',
        blank=True,
        null=True,
        help_text='upcoming class'
    )
    log = models.ForeignKey(
        ClassLog,
        verbose_name='Log',
        on_delete=models.DO_NOTHING,
        related_name='entries',
        blank=True,
        null=True,
        help_text='passed class'
    )
    user_pass = models.ForeignKey(
        UserPass,
        verbose_name='User Pass',
        on_delete=models.DO_NOTHING,
        related_name='entries'
    )

    @cached_property
    def entry_class(self):
        if self.schedule:
            return self.schedule
        return self.log

    class Meta:
        verbose_name = 'User Entry'
        verbose_name_plural = 'User Entries'
