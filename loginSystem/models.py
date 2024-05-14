from django.db import models

# Create your models here.
class Logsystem(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=2500)
    password = models.CharField(max_length=2500)