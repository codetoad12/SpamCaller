from django.shortcuts import render

from rest_framework.response import Response
from .models import Spam,Contacts,UserContacts,User
from .serializers import SpamSerializer,SearchByNameSerializer,SearchByPhoneSerializer,ContactSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

class ReportSpam(CreateAPIView):
    queryset=Spam.objects.all()
    serializer_class=SpamSerializer
    permission_classes=[IsAuthenticated]

class CreateContact(CreateAPIView):
    queryset=Contacts.objects.all()
    serializer_class=ContactSerializer
    permission_classes=[IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer=ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        model=UserContacts()
        data = Contacts.objects.filter(phone_number=serializer.data['phone_number'])
      
        model.contact_id=data[0]
        user=request.user.id
        
        user_instance=User.objects.filter(id=user)
        model.user_id= user_instance[0]
        model.save()
        return Response(serializer.data)

class SearchByName(CreateAPIView):
    serializer_class=SearchByNameSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer=SearchByNameSerializer(data=request.data)
        serializer.is_valid()
        start_names=Contacts.objects.filter(name__startswith=serializer.data['name'])
        contains_names=Contacts.objects.filter(name__icontains=serializer.data['name'])
        all_names=[]

        for item_one in start_names:
            all_names.append(item_one)

        for item_two in contains_names:
            if(item_two not in all_names):
                all_names.append(item_two)        
        li=[]
        counter=0
        contacts_length=len(Contacts.objects.all())
        spam_model=Spam.objects.all()
        spam_likelihood=[]

        for obj in all_names:      
            counter=0 
            for spam in spam_model:
                if(spam.contact_id==None):
                    pass
                elif(spam.contact_id.id==obj.id):
                    counter+=1
            spam_likelihood.append(counter/contacts_length)

        index=0
        for name in all_names:
            n=name.name
            ph=name.phone_number
            di={"name":n,"phone_number":ph,"spam_likelihood":spam_likelihood[index]}
            li.append(di)
            index+=1
        context={"data":li}
        return Response(context)


class SearchByPhone(CreateAPIView):
    serializer_class=SearchByPhoneSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer=SearchByPhoneSerializer(data=request.data)
        serializer.is_valid()
     
        spam_model=Spam.objects.all()
        user_phone=User.objects.filter(phone_number=serializer.data['phone'])
        
        contacts_length=len(Contacts.objects.all())
        if(user_phone.exists()):
            li=[]
            for spam in spam_model:
                counter=0
                for obj in user_phone:   
                    if(spam.contact_id==None):
                        pass
                    elif(spam.contact_id.id==obj.id):
                        counter+=1
            spam_likelihood=counter/contacts_length

            for item in user_phone:
                name=item.first_name
                phone=item.phone_number
                email=item.email
                di={"name":name,"phone_number":phone,"email":email,'spam_likelihood':spam_likelihood}
                li.append(di)
            context={"data":li}
        
        else:
            print("user not existing")
            number=Contacts.objects.filter(phone_number=serializer.data['phone'])
            li=[]
            counter=0
            for spam in spam_model:

                for obj in number:   
                    if(spam.contact_id==None):
                        pass
        
                    elif(spam.contact_id.id==obj.id):
                        counter+=1
            spam_likelihood=counter/contacts_length
         
            for item in number:
                name=item.name
                phone=item.phone_number
                di={"name":name,"phone_number":phone,"spam_likelihood":spam_likelihood}
                li.append(di)
            context={"data":li}
            
        return Response(context)
