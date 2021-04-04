from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField, ImageSpecField
from model_utils.models import TimeStampedModel

from solf.apps.business.models import Fitness
from solf.apps.common.models import WeekdayTimeMixin
from solf.apps.common.utils import image_specs
from solf.apps.common.utils.file_extension_validators import IMAGE_ALLOWED_EXTENSIONS
from solf.apps.core.models import Category


class Class(TimeStampedModel):

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


class ClassSchedule(TimeStampedModel, WeekdayTimeMixin):
    class_template = models.ForeignKey(
        Class,
        verbose_name='Class',
        on_delete=models.CASCADE,
        related_name='schedule',
    )
    max_spots = models.PositiveSmallIntegerField(
        verbose_name='Maximum available spots'
    )

    class Meta:
        verbose_name = 'Class Schedule'
        verbose_name_plural = 'Classes Schedule'


# TODO: Придумать флоу когда текущие занятия перекидываются в логи
class ClassScheduleLogs(TimeStampedModel):
    schedule = models.ForeignKey(
        ClassSchedule,
        verbose_name='Schedule',
        on_delete=models.DO_NOTHING,
        related_name='logs'
    )

    class Meta:
        verbose_name = 'Class Schedule Logs'
        verbose_name_plural = 'Classes Schedule Logs'

# TODO: Придумать каким образом будем хранить записи for upcoming classes and passed classes
# class ClassUserEntry(TimeStampedModel):
#     schedule = models.ForeignKey(
#         ClassSchedule,
#         verbose_name='Schedule',
#         on_delete=models.DO_NOTHING,
#         related_name='entries'
#     )
#     user = models.ForeignKey(
#         User,
#         verbose_name='User',
#         on_delete=models.DO_NOTHING,
#         related_name='entries'
#     )
