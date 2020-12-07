from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('last_login', 'email', 'password')
    list_display = ('email', 'is_staff', 'is_superuser')


admin.site.register(User, UserAdmin)