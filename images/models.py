from django.db import models
from datetime import datetime
import os

# Create your models here.

def get_file_path(instance, filename):
    now = datetime.now()
    return os.path.join("images", f"{now.year}/{now.month}/{now.day}/", filename)


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    upload_date = models.DateTimeField(default=datetime.now)
    file = models.ImageField(upload_to=get_file_path, blank=True)


    def __str__(self):
        return self.title 
