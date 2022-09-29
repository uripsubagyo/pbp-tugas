from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length = 255)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_finised = models.TextField()
