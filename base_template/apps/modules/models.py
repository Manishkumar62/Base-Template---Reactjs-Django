from django.db import models


class Module(models.Model):
    """
    Module model for dynamic sidebar navigation.
    Each module represents a menu item in the frontend.
    """
    
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'dashboard', 'users', 'settings'
    path = models.CharField(max_length=200)  # e.g., '/dashboard', '/users'
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    order = models.IntegerField(default=0)  # For sorting menu items
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'modules'
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class RoleModulePermission(models.Model):
    """
    Maps roles to modules with specific permissions.
    Controls what each role can do in each module.
    """
    
    role = models.ForeignKey(
        'roles.Role',
        on_delete=models.CASCADE,
        related_name='module_permissions'
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='role_permissions'
    )
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'role_module_permissions'
        verbose_name = 'Role Module Permission'
        verbose_name_plural = 'Role Module Permissions'
        unique_together = ('role', 'module')
    
    def __str__(self):
        return f"{self.role.name} - {self.module.name}"