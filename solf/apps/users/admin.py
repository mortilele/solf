from django.contrib import admin

from solf.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
