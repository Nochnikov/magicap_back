from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if not username:
            raise ValueError("The given username must be set")

        user = self.model(username=username, **extra_fields)
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):

        return self.create_user(username, password, is_staff=True, is_superuser=True, **extra_fields)







