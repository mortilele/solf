from django.contrib import admin

from solf.apps.classes import models


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClassLog)
class ClassLogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClassUserEntry)
class ClasUserEntry(admin.ModelAdmin):
    pass
