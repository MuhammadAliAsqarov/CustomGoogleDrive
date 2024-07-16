from django.contrib.auth.hashers import check_password, make_password
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User
from .serializers import UserRegisterSerializer
from .permissions import IsSuperAdminOrHR


class UserViewSet(viewsets.ViewSet):

    @permission_classes([IsSuperAdminOrHR])
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([AllowAny])
    def login(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'message': 'User not found', 'ok': False}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.password):
            return Response({'error': 'Incorrect password', 'ok': False}, status=status.HTTP_400_BAD_REQUEST)

        # Authentication successful, generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token, 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)

    def logout(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'Refresh token not provided', 'ok': False}, status=status.HTTP_400_BAD_REQUEST)
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Token has been added to blacklist', 'ok': True},
                        status=status.HTTP_205_RESET_CONTENT)
