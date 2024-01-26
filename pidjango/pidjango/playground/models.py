from django.db import models

# Create your models here.


class File(models.Model):
    # Model for a file
    name = models.CharField(max_length=255)
    path = models.FileField(upload_to='pidjango/media')
