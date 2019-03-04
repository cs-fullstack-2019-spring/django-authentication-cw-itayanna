from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for account sign up

class foodInfo(models.Model):
    username = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    date = models.DateField(default=None)
    linkedAccount = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


