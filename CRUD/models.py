from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=2500)
    job = models.CharField(max_length=3400)
    def __str__(self):
        return self.name
    