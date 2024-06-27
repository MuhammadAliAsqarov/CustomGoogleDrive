from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FileGroup(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class File(models.Model):
    file = models.FileField(upload_to='files/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(FileGroup, on_delete=models.CASCADE, null=True, blank=True)
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)

    def __str__(self):
        return str(self.file)
