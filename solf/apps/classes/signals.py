from django.db.models.signals import post_save
from django.dispatch import receiver

from solf.apps.classes.models import Class, ClassSchedule, ClassUserEntry


@receiver(post_save, sender=Class)
def cancel_class_schedules(sender, instance, **kwargs):
    if not instance.is_active:
        for class_schedule in instance.classschedules:
            class_schedule.is_active = False
            # Triggers ClassSchedule's signal
            class_schedule.save(update_fields=['is_active'])


@receiver(post_save, sender=ClassSchedule)
def cancel_class_schedules(sender, instance, **kwargs):
    if not instance.is_active:
        ClassUserEntry.objects.filter(
            schedule_id=instance.id,
            status=ClassUserEntry.EntryStatus.WAITING.value
        ).update(
            status=ClassUserEntry.EntryStatus.CANCELED_BY_MODERATOR.value
        )
