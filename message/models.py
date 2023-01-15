from django.db import models

# Create your models here.
class Img(models.Model):
    name = models.CharField(max_length=30)
    picture = models.FileField(upload_to='media/')


class Upload(models.Model):
    content = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255, null=True)
    time = models.DateTimeField(auto_now=True)
