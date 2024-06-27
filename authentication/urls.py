from django.urls import path
from .views import AuthViewSet

auth_view_set = AuthViewSet.as_view({
    'post': 'register'
})
auth_login = AuthViewSet.as_view({
    'post': 'login'
})
auth_logout = AuthViewSet.as_view({
    'post': 'logout'
})

urlpatterns = [
    path('register/', auth_view_set, name='register'),
    path('login/', auth_login, name='login'),
    path('logout/', auth_logout, name='logout'),
]
