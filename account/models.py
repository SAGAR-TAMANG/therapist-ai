from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  
  class Meta:
      swappable = 'AUTH_USER_MODEL'
