from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """ Custom permission to only allow admin users to edit or delete products. """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
