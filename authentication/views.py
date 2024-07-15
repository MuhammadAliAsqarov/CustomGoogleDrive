from django.contrib.auth.hashers import check_password, make_password
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User
from .serializers import UserRegisterSerializer
from .permissions import IsSuperAdminOrHR, IsEmployee


class UserViewSet(viewsets.ViewSet):
    @permission_classes([IsSuperAdminOrHR])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsEmployee])
    def login(self, request):
        data = request.data
        user = User.objects.filter(username=data['username']).first()
        if not user:
            return Response({'message': 'User not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)
        if check_password(data['password'], user.password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token, 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
        return Response({'error': 'Incorrect password', 'ok': False}, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsEmployee])
    def logout(self, request):
        data = request.data
        refresh_token = data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            if BlacklistedToken.objects.filter(token=token).exists():
                return Response({'error': 'Token is already blacklisted', 'ok': False},
                                status=status.HTTP_400_BAD_REQUEST)
            token.blacklist()
            return Response({'message': 'Token has been added to blacklist', 'ok': True},
                            status=status.HTTP_205_RESET_CONTENT)
        return Response({'error': 'Refresh token not provided', 'ok': False}, status=status.HTTP_400_BAD_REQUEST)
