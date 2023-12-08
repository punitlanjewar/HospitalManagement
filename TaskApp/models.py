from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile')
    user_address = models.TextField()
    user_city = models.CharField(max_length=100)
    user_lane = models.CharField(max_length=100)
    user_state = models.CharField(max_length=100)
    user_pincode = models.IntegerField()