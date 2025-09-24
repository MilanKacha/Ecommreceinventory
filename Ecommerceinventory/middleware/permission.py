from rest_framework.permissions import BasePermission
from rest_framework import status
from Ecommerceinventory.Helpers import renderResponse


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role') and request.user.role == 'Super Admin': #hasattr checks if user has role attribute
            return True # Allow access if user is SuperAdmin
        return False # Deny access otherwise
    
    def __call__(self, request):
        if not self.has_permission(request, None):
            return renderResponse(
                data=None,
                message="You do not have permission to perform this action.",
                status=status.HTTP_403_FORBIDDEN
            )
        return None