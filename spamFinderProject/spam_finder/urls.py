from rest_framework.routers import DefaultRouter
from . import views 
from django.urls import path

router =DefaultRouter()

#router.register('spam',views.SpamViewSet)
#router.register('contacts',views.ContactViewSet)

urlpatterns=[path('contact/',views.CreateContact.as_view(),name='contacts'),
             path('spam/',views.ReportSpam.as_view()),
             path('search-name/',views.SearchByName.as_view()),
             path('search-phone/',views.SearchByPhone.as_view())]