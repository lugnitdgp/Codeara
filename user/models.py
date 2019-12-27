from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User_profile(models.Model):
  name = models.CharField(max_length=200, blank=True)
  #user = models.OneToOneField(User)
  #image = models.ImageField(upload_to=get_image_path, blank=True,null=True)



  def __str__(self):
    return self.name