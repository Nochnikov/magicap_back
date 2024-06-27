from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    ADMIN, HR, EMPLOYEE = 1, 2, 3

    ROLE_CHOICE = (
        (ADMIN, 'Admin'),
        (HR, 'HR'),
        (EMPLOYEE, 'Employee'),
    )
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    coins = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=ROLE_CHOICE, default=EMPLOYEE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []










