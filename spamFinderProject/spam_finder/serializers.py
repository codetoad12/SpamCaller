from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import Contacts,Spam,UserContacts,User


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','username','password','phone_number','email','first_name']

class SpamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Spam
        fields=['contact_id','reported_by']

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contacts
        fields=['id','phone_number','name']
    
class SearchByNameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=255)

class SearchByPhoneSerializer(serializers.Serializer):
    phone=serializers.IntegerField()