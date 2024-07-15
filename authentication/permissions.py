from rest_framework.permissions import BasePermission


class IsSuperAdminOrHR(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [1, 2]


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [1, 2, 3, 4]
