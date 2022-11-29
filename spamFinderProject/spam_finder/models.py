from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
class User(AbstractUser):

    phone_number=models.IntegerField()

class Contacts(models.Model):
    
    name=models.CharField(max_length=256)
    phone_number=models.IntegerField() 

class UserContacts(models.Model):

    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_id=models.ForeignKey(Contacts,on_delete=models.CASCADE)

class Spam(models.Model):

    reported_by=models.ForeignKey(User,on_delete=models.PROTECT,null=True)
    contact_id=models.ForeignKey(Contacts,on_delete=models.PROTECT,null=True)

