from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todolist(models.Model):
    todoname = models.CharField(max_length=100)
    tododesc = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.todoname