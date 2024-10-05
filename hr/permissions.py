from rest_framework.permissions import BasePermission, DjangoModelPermissions




class IsHRorAdmin(BasePermission):
    def has_permission(self, request, view):
        role = request.user.role
        if role == 1 or role == 2:
            return True
        else:
            return False

