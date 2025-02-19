from rest_framework.permissions import BasePermission

class SuperuserOnly(BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        """
        Only admin permission
        """
        return request.user.is_authenticated and request.user.role == 'superuser'