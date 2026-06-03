from django.db import models


class Audio(models.Model):

    name = models.CharField(max_length=200)

    song = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.name