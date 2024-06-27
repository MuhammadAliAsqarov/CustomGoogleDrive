from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import File, FileGroup
from .serializers import FileSerializer, FileGroupSerializer


class FileGroupViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='List all file groups',
        operation_summary='List all file',
        responses={200: FileGroupSerializer(many=True)},
    )
    def list(self, request):
        groups = FileGroup.objects.filter(owner=request.user)
        serializer = FileGroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Create a file group',
        operation_summary='Add a file group',
        request_body=FileGroupSerializer,
        responses={201: FileGroupSerializer, 400: 'Bad Request'}
    )
    def create(self, request):
        serializer = FileGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Retrieve a file group',
        operation_summary='Get a file group',
        responses={200: FileGroupSerializer,
                   404: 'FileGroup not Found'
                   }
    )
    def retrieve(self, request, pk):
        group = FileGroup.objects.filter(pk=pk, owner=request.user)
        if not group.exists():
            return Response(data={'error': 'FileGroup not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FileGroupSerializer(group.first())
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Update a file group',
        operation_summary='Update file group',
        request_body=FileGroupSerializer,
        responses={200: FileGroupSerializer,
                   400: 'Bad Request',
                   404: 'FileGroup not found'}
    )
    def update(self, request, pk):
        group = FileGroup.objects.filter(pk=pk, owner=request.user)
        if not group.exists():
            return Response(data={'error': 'FileGroup not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FileGroupSerializer(group.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Delete a file group',
        operation_summary='Delete file group',
        responses={204: 'FileGroup deleted successfully',
                   404: 'FileGroup not found'}
    )
    def delete(self, request, pk):
        group = FileGroup.objects.filter(pk=pk, owner=request.user)
        if not group.exists():
            return Response(data={'error': 'FileGroup not found'}, status=status.HTTP_404_NOT_FOUND)
        group.first().delete()
        return Response(data={'message': 'FileGroup deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class FileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='List all files',
        operation_summary='Get files',
        responses={200: FileSerializer(many=True)
                   }
    )
    def list_files(self, request):
        files = File.objects.filter(owner=request.user)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Upload a file',
        operation_summary='Add file',
        request_body=FileSerializer,
        responses={201: FileSerializer,
                   400: 'Bad Request'
                   }

    )
    def upload_file(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Retrieve a file',
        operation_summary='Get file',
        responses={200: FileSerializer,
                   404: 'Not Found'
                   }
    )
    def retrieve_file(self, request, pk):
        file = File.objects.filter(pk=pk, owner=request.user)
        if not file.exists():
            return Response(data={'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file.first())
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Update a file',
        operation_summary='Update file',
        request_body=FileSerializer,
        responses={200: FileSerializer,
                   400: 'Bad Request',
                   404: 'File not found'
                   }
    )
    def update_file(self, request, pk):
        file = File.objects.filter(pk=pk, owner=request.user)
        if not file.exists():
            return Response(data={'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Delete a file',
        operation_summary='Delete file',
        responses={204: 'File deleted successfully',
                   404: 'File Not Found'
                   }
    )
    def delete_file(self, request, pk):
        file = File.objects.filter(pk=pk, owner=request.user)
        if not file.exists():
            return Response(data={'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        file.first().delete()
        return Response(data={'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
