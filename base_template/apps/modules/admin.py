from django.contrib import admin
from .models import Module, RoleModulePermission


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'icon', 'parent', 'order', 'is_active')
    list_filter = ('is_active', 'parent')
    search_fields = ('name', 'path')
    ordering = ('order', 'name')


@admin.register(RoleModulePermission)
class RoleModulePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'module', 'can_view', 'can_add', 'can_edit', 'can_delete')
    list_filter = ('role', 'module', 'can_view', 'can_add', 'can_edit', 'can_delete')
    search_fields = ('role__name', 'module__name')