from django.contrib import admin

# Register your models here.
from solf.apps.core import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
