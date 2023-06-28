from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name']
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('email', 'username', 'first_name',
                               'last_name', 'password1', 'password2', ),
                },
            ),
        )


admin.site.register(CustomUser, CustomUserAdmin)
