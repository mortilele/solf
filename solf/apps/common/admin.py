from django.contrib import admin

# Register your models here.
from solf.apps.common import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass
