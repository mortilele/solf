from django.contrib import admin

from solf.apps.users.models import User, UserPass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPass)
class UserPassAdmin(admin.ModelAdmin):
    pass
