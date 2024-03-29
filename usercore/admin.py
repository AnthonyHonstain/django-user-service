from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age")


admin.site.register(User, UserAdmin)
