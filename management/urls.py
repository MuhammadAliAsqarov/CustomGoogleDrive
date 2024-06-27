from django.urls import path
from .views import FileGroupViewSet, FileViewSet

file_group_list = FileGroupViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
file_group_detail = FileGroupViewSet.as_view({
    'get': 'list_group_files',
    'put': 'update',
    'delete': 'delete'
})

file_list = FileViewSet.as_view({
    'get': 'list_files',
    'post': 'upload_file'
})
file_detail = FileViewSet.as_view({
    'get': 'retrieve_file',
    'put': 'update_file',
    'delete': 'delete_file'
})

urlpatterns = [
    path('file-groups/', file_group_list, name='file-group-list'),
    path('file-groups/<int:pk>/', file_group_detail, name='file-group-detail'),
    path('files/', file_list, name='file-list'),
    path('files/<int:pk>/', file_detail, name='file-detail'),
    path('files/shared/', FileViewSet.as_view({'get': 'list_shared_with_me'}), name='file-detail'),
]
