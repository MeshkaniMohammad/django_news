from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('ایمیل الزامی است')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user



class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'email'

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

