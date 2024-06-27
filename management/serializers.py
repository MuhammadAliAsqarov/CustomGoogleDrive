from rest_framework import serializers
from .models import File, FileGroup


class FileGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileGroup
        fields = ['name']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file', 'group', 'shared_with']
