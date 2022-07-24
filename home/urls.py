from django.conf import settings
from django.urls import path
from home import views
from .api_app_views import GetAllContacts, GetDataFromMultipleTable, GetSinglwContact, GetSomeDataFromContacts, UserContact, UserContactDelete, UserContactUpdate


urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("customer", views.customer, name='customer'),
    path("view_database", views.view_database, name='contact'),
    path("view_customers", views.view_customers, name='view_customers'),
    path("view_plants", views.view_plants, name='view_plants'),
    
    path("flutter_1", views.flutter_1, name='flutter_1'),
    path("flutter_2", views.flutter_2, name='flutter_2'),
    path("flutter_3", views.flutter_3, name='flutter_3'),

    path('contact_save_from_postman/', UserContact.as_view()),# working
    path('contact_update_from_postman/', UserContactUpdate.as_view()),# working
    path('contact_delete_from_postman/', UserContactDelete.as_view()),# working
    path('get_contacts/', GetAllContacts.as_view()),# 
    path('get_someinfo_from_contact/', GetSomeDataFromContacts.as_view()),# 
    path('get_data_from_multiple_tables/', GetDataFromMultipleTable.as_view()),# 
    path('get_contact/', GetSinglwContact.as_view()),# 
   
    path("get_contacts_as_json", views.get_contacts_as_json, name='get_contacts_as_json'),# we are getting 2 values only from model
    path('getall_contacts/', views.getall_contacts, name='getall_contacts'),# working
    path('getSingle_contacts/', views.getSingle_contacts, name='getSingle_contacts'),
    
    
    
]
#https://stackabuse.com/creating-a-rest-api-in-python-with-django/