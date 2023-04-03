from django.db import models
from django.db.models.fields import DecimalField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Extra
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.conf import settings

class User(AbstractBaseUser,PermissionsMixin):
    # first_name =models.CharField(max_length=250)
    email = models.EmailField(_('email address'), unique=True)
    mobile =models.CharField(max_length=10)
    u_name = models.CharField(max_length=100)
    u_location = models.CharField(max_length=100)
    u_login = models.CharField(max_length=100)
    u_rights = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    object =CustomUserManager()
    def __str__(self):
        return self.u_name


class Appliance(models.Model):
    id = models.BigAutoField(primary_key=True)
    A_name = models.CharField(max_length=100)
    A_category = models.CharField(max_length=100)
    A_watt = models.DecimalField(max_digits=13 , decimal_places=2) 
    A_consumption = models.DecimalField(max_digits=13 , decimal_places=2)
    Forkey = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.A_name
