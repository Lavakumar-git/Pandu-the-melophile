from django.db import models

class Audio(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    song = models.FileField(upload_to='songs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name