from django.contrib import admin
from .models import User,Spam,Contacts,UserContacts
# Register your models here.
admin.site.register(User)
admin.site.register(Spam)
admin.site.register(Contacts)
admin.site.register(UserContacts)