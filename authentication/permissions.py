from rest_framework.permissions import BasePermission



def is_super_admin_or_hr(func):
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise CustomApiException(error_code=ErrorCodes.UNAUTHORIZED.value)
        elif request.user.role in [3, 4]:
            return func(self, request, *args, **kwargs)
        raise CustomApiException(error_code=ErrorCodes.FORBIDDEN.value)

    return wrapper