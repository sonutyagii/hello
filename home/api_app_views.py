from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from home.models import Contact
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import (get_object_or_404,render, HttpResponseRedirect)

@method_decorator(csrf_exempt, name='dispatch')

class UserContact(View):# here we are saving contact data( from api) in Django DB which we can read & updat from admin
    # run below code from postman row
#         {
# 	"email": "sonutyagi.1126@gmail.com",
# 	"address": "4",
# 	"somthing_else": "postman desc from postman id 4 ",
# 	"date": "2021-12-31"
# }
    
    def post(self, request):


         data = json.loads(request.body.decode("utf-8"))
         email = data.get('email')
         address = data.get('address')
         somthing_else = data.get('somthing_else')
         date = data.get('date')

         contact_data = {
            'email': email,
            'address': address,
            'somthing_else': somthing_else,
            'date': datetime.fromisoformat(date)
            
        }

         contact_item = Contact.objects.create(**contact_data)

         data = {
            "message": f"New item added "
          #  "message": f"New item added to Cart with id: {contact_data.email}"
        }
         return JsonResponse(data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class UserContactUpdate(View):# here we are updating contact data( from api) in Django DB which we can read & updat from admin
     # run below code from postman row
#     {
# 	"email": "09_postan2_jul_sonutyagi.1126@gmail.com",
# 	"address": "update address from postman",
# 	"somthing_else": "update somthing else from postman",
# 	"date": "2022-07-22"
# }
    
    
    def post(self, request):
         data = json.loads(request.body.decode("utf-8"))
         email = data.get('email')
         address = data.get('address')
         somthing_else = data.get('somthing_else')
         date = data.get('date')
        
         Contact.objects.filter(email=email).update(address=address,somthing_else=somthing_else,date=date)
         
         data = {
            "message": f"Item updated "
            
        }
         return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UserContactDelete(View):# here we are deleting contact data( from api) in Django DB which we can read & updat from admin
  
    def post(self, request):
         data = json.loads(request.body.decode("utf-8"))
         email = data.get('email')

         if Contact.objects.filter(email=email).exists():
          
          data_to_be_deleted = Contact.objects.filter(email = email)
          data_to_be_deleted.delete()
          data = {
            "message": f"Item Deleted ",
             "data":list(Contact.objects.values())
            
        }
          
          return JsonResponse(data, status=200)
   
         else:
          data = {
            "message": f"Not Exist"
            
        }
          return JsonResponse(data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class GetAllContacts(View):# here we are getting all the data from contact table( from api) in Django DB which we can read & updat from admin
  
    def get(self, request):
          data = list(Contact.objects.values())
          return JsonResponse({'success': 200,'today': datetime.today(), 'data': data})
       
  
@method_decorator(csrf_exempt, name='dispatch')
class GetSinglwContact(View):# here we are getting single item from contact table( from api) in Django DB which we can read & updat from admin
  
     def get(self, request):
         user = Contact.objects.get(email="postman_B_02Jul_sonutyagi.1126@gmail.com")
         return user.email
        
       
  