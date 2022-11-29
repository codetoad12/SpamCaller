from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number=models.IntegerField(unique=True)
    REQUIRED_FIELDS = ["phone_number","username"]

