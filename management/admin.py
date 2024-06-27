from django.contrib import admin
from .models import File, FileGroup


class FileGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'owner', 'group')


admin.site.register(File, FileAdmin)
admin.site.register(FileGroup, FileGroupAdmin)
