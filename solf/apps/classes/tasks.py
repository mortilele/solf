from datetime import datetime

from celery import shared_task
from django.utils import timezone

from solf.apps.classes import services
from solf.apps.classes.models import ClassSchedule


@shared_task(default_retry_delay=2 * 60, max_retries=2)
def update_passed_class_schedules():
    current_time = timezone.now().time()
    current_weekday = datetime.now().weekday()
    passed_class_schedules = ClassSchedule.objects.filter(
        weekday=current_weekday + 1,
        end_time__lte=current_time,
    )
    for passed_class_schedule in passed_class_schedules:
        services.transfer_schedule_to_logs(class_schedule=passed_class_schedule)
