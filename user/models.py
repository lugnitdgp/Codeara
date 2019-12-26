from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=250)
    ques = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    source_code = models.CharField(max_length=4500)
    