from django.contrib import admin

# Register your models here.
from solf.apps.core.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass