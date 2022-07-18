from math import ceil
from django.conf import settings
from email import message
from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import render , HttpResponse
from matplotlib.style import context
from datetime import datetime
from django.core import serializers
from home.models import Contact, Customer
# Create your views here.

def index(request):
    # here context is the dict to send the data to template. we will use this for fetching data from db 
    context = {
        "variable":"my first variable"
    }
    return render(request,'index.html' , context)
    # return HttpResponse('this is home page')


def about(request):
    return render(request,'about.html')

def flutter_1(request):
    return render(request,'flutter_1.html')


def flutter_2(request):
    return render(request,'flutter_2.html')



def flutter_3(request):
    return render(request,'flutter_3.html')


# def getall_contacts(request): # here we fetching all contacts ( from get method) in Django DB which we can read & updat from admin
#     #http://127.0.0.1:8000/getall_contacts/
#     if request.method == "GET":
#      data = list(Contact.objects.values())
     
#      return JsonResponse({'success': 200,'today': datetime.today(), 'data': data})
     
#     else:
#      return "Contacts Not Found"   
 

def getSingle_contacts(request): # here we are fetching single contact with id ( from get method) in Django DB which we can read & updat from admin
    if request.method == "GET":
     data = Contact.objects.get(email='09_jul_sonutyagi.1126@gmail.com')
     
     return data
     
    else:
     return "Not Found"   
 


def contact(request): # here we are creating & saving single contact ( from fourm) in Django DB which we can read & updat from admin
    if request.method == "POST":
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        somthong_else = request.POST.get('somthong_else')
        contact = Contact(email=email , address=address , somthing_else=somthong_else, mobile=mobile, date=datetime.today())
        contact.save()
        
    return render(request,'contact.html') 
    

def view_database(request): # here we are fetching data from database and listing on html page
    if request.method == "GET":
        data = Contact.objects.all()
        # n = len(data)
        # nSlides = n//4 * ceil((n/4)-(n//4))
        # params = {'number_of_slides':nSlides, 'range':range(nSlides),'data': data}
        params = {'data': data}

    return render(request, 'contact_numbers.html', params)
    #return render(request, 'contact_numbers.html', context)

   # first_name ,last_name  ,customer_email ,city ,state ,zip
def customer(request): # here we are creating & saving single customer ( from fourm) in Django DB which we can read & updat from admin
    if request.method == "POST":
        first_name = request.POST.get('validationDefault01')
        last_name = request.POST.get('validationDefault02')
        customer_email = request.POST.get('validationDefaultUsername')
        city = request.POST.get('validationDefault03')
        state = request.POST.get('validationDefault04')
        zip = request.POST.get('validationDefault05')
        
    
    
        #first_name = "a"
        # last_name ="b"
        # customer_email ="c"
        # city = "d"
        # state = "manual state"
        # zip = "f"
        
        customer = Customer(first_name=first_name , last_name=last_name 
        , customer_email=customer_email , city=city, state=state , zip=zip
        , date=datetime.today())
        customer.save()
        
    return render(request,'customer.html') 


def view_customers(request): # here we are fetching data from database and listing on html page
    if request.method == "GET":
        data = Customer.objects.all()
       
        params = {'data': data}

    return render(request, 'view_customers.html', params)