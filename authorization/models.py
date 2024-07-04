from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from authorization.managers import UserManager
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
    email = models.EmailField(null=True)
    role = models.IntegerField(choices=ROLE_CHOICE, default=EMPLOYEE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)









