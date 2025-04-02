from rest_framework.permissions import BasePermission

class SuperuserOnly(BasePermission):
    def has_permission(self, request, view):
        """
        Only admin permission
        """
        return request.user.is_authenticated and request.user.role == 'superuser'
    
class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['superuser', 'admin']