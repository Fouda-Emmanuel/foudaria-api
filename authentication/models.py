from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser should have is_staff as True'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser should have is_superuser as True'))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser should have is_active as True'))
        
        return self.create_user(email, password, **extra_fields) 
    

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(unique=True, null=False)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username','phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

        
    
    

