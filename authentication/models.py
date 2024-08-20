from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.tz import localtime

ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Accountant'),
    (3, 'HR'),
    (4, 'SuperAdmin'),
)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)
    kpi = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    fixed_salary = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)

    def __str__(self):
        return self.username


class UserTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_timestamp = localtime(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        user_display = self.user.username if self.user else 'Anonymous'
        return f"{user_display} accessed {self.path} on {formatted_timestamp}"
