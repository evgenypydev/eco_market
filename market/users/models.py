from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
