from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password, make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model, authenticate, login, logout
from .serializers import UserSerializer
from drf_yasg import openapi

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'register': [AllowAny],
        'login': [AllowAny],
        'logout': [IsAuthenticated],
    }

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: openapi.Response('User registered successfully'),
            400: openapi.Response('Bad Request')
        }
    )
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.password = make_password(user.password)
            user.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=UserSerializer(),
        responses={200: openapi.Response(
            description='Successful',
            schema=openapi.Schema(type=openapi.TYPE_OBJECT,
                                  properties={
                                      'access_token': openapi.Schema(type=openapi.TYPE_STRING,
                                                                     description='access_token'),
                                      "refresh_token": openapi.Schema(type=openapi.TYPE_STRING,
                                                                      description="refresh_token")}))},
    )
    def login(self, request):
        data = request.data
        user = User.objects.filter(username=data['username']).first()
        if not user:
            return Response({'error': 'User not found', 'ok': False}, status=status.HTTP_400_BAD_REQUEST)
        if check_password(data['password'], user.password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token, 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
        return Response({'error': 'invalid password', 'ok': False}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            200: openapi.Response('User logged out successfully')
        }
    )
    def logout(self, request):
        logout(request)
        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
