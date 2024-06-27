from rest_framework import permissions


class IsOwnerOrSharedWith(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the file
        if request.user == obj.owner:
            return True

        # Check if the user is in the shared_with field
        if request.user in obj.shared_with.all():
            # Disallow editing for shared users
            if view.action in ['update', 'partial_update']:
                return False
            return True

        # Default deny permission
        return False
