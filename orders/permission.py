from rest_framework.permissions import BasePermission

class CustomIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser