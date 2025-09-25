from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class User(AbstractUser): 
     phone_number = models.CharField(max_length=15, blank=True, null=True) 
     # text = models.CharField(max_length=15, blank=True, null=True)
     
     class Meta: 
          db_table = 'mc_users'
