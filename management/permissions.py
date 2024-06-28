from rest_framework import permissions
from django.db.models import QuerySet


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If obj is a queryset, get the first instance
        if isinstance(obj, QuerySet):
            obj = obj.first()

        # Check if the user is the owner of the file
        if request.user == obj.owner:
            return True
        # Default deny permission
        return False


class IsOwnerOrSharedWith(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If obj is a queryset, get the first instance
        if isinstance(obj, QuerySet):
            obj = obj.first()

        # Check if the user is the owner of the file
        if request.user == obj.owner:
            return True

        # Check if the user is in the shared_with field
        if request.user in obj.shared_with.all():
            # Allow read-only actions for shared users
            if view.action in ['retrieve_file', 'list_files', 'update_file']:
                return True
            # Deny write actions for shared users
            return False

        # Deny access if neither owner nor shared_with
        return False
