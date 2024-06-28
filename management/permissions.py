from rest_framework import permissions


class IsOwnerOrSharedWith(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the file
        if request.user == obj.first().owner:
            return True
        # Check if the user is in the shared_with field
        if request.user in obj.first().shared_with.all():
            if view.action in ['GET', 'PUT', 'PATCH']:
                return False
            return True

        return False
