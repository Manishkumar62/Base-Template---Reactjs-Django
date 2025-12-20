from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom User Admin configuration.
    """
    
    list_display = ('username', 'email', 'role', 'department', 'phone', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_active', 'is_staff', 'role', 'department', 'created_at')
    search_fields = ('username', 'email', 'phone', 'employee_id')
    ordering = ('-created_at',)
    
    # Fields shown when viewing/editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone', 'employee_id', 'role', 'department',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields shown when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'department', 'is_staff', 'is_active'),
        }),
    )