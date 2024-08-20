from django.contrib import admin
from .models import User, UserTracking


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


class UserTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp')


admin.site.register(User, UserAdmin)
admin.site.register(UserTracking)
