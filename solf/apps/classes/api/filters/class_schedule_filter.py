import django_filters

from solf.apps.classes.models import ClassSchedule


class ClassScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = ClassSchedule
        fields = [
            'weekday',
            'start_time',
            'end_time',
            'class_template',
            'class_template__fitness',
            'class_template__category',
        ]
