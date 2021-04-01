from django.contrib import admin
# Register your models here.
from solf.apps.classes import models


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    pass

