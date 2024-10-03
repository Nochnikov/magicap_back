from rest_framework.permissions import BasePermission, DjangoModelPermissions




class IsHRorAdmin(BasePermission):
    def has_permission(self, request, view):
        role = request.user.role

        if role == 'Admin' or role == 'HR':
            return True
        else:
            return False