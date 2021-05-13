from solf.apps.classes.models import ClassSchedule, ClassUserEntry, ClassLog
from solf.apps.common.utils import messages
from solf.apps.common.utils.exceptions import SolfAPIException
from solf.apps.users.models import User


def sign_up_to_class(class_schedule: ClassSchedule, user: User):
    user_pass = user.passes.first()
    if ClassUserEntry.objects.filter(
            schedule_id=class_schedule.id,
            user_pass=user_pass
    ).exists():
        raise SolfAPIException(detail=messages.ALREADY_SIGNED_UP)

    user_entry = ClassUserEntry.objects.create(
        schedule_id=class_schedule.id,
        user_pass=user_pass
    )
    return user_entry


def transfer_schedule_to_logs(class_schedule: ClassSchedule):
    log = ClassLog.objects.create(
        weekday=class_schedule.weekday,
        start_time=class_schedule.start_time,
        end_time=class_schedule.end_time,
        one_entry_price=class_schedule.class_template.one_entry_price,
        entry_type=class_schedule.class_template.entry_type,
        class_template=class_schedule.class_template,
        max_spots=class_schedule.max_spots,
        schedule=class_schedule
    )
    ClassUserEntry.objects.filter(
        schedule_id=class_schedule.id
    ).update(
        log_id=log.id
    )

