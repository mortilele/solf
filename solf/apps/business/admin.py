from django.contrib import admin

# Register your models here.
from solf.apps.business import models


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Fitness)
class FitnessAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
