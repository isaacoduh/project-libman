from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


class UserAdmin(BaseAdmin):
    """Customize admin overview for the User model"""
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_librarian']
    list_filter = ['is_staff', 'is_librarian']

    fieldsets = (
        (_("Personal Info"), {"fields": ("email", "first_name", "last_name", "password")}),
        (_("Permissions"),
         {"fields": ("is_active", "is_staff", "is_superuser", "is_librarian", "groups", "user_permissions")})
    )

    add_fieldsets = (
        (_("Create User"), {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password", "is_librarian")
        })
    )
    search_fields = ['email', 'first_name', 'last_name']
    readonly_fields = ['last_login']


admin.site.register(User, UserAdmin)
