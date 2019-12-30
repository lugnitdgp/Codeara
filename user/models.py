from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User_profile(models.Model):
  first_name = models.CharField(max_length=200, blank=True)
  user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
  n_subm = models.IntegerField(default=0)
  n_s_sub = models.IntegerField(default=0)
  lang = models.CharField(max_length=400,blank=True)

  def __str__(self):
    return self.first_name