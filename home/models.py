from operator import mod
from django.db import models
from django.forms import ValidationError
from flask import Response
from itsdangerous import Serializer
from rest_framework import serializers


# creating a validator function
def validate_geeks_mail(inputValue):
    #dict = {'1': '@gmail.com', '2': '@yahu.com', '3': '@international.in'}
    #if inputValue in dict.values():   a
    if '@gmail.com' in inputValue:
        return inputValue
    else:
        raise ValidationError("This field accepts mail id of gmail.com|yahu.com|international.in only")


def upload_image(self, filename):
       # return 'post/{}/{}'.format(self.title, filename)
       return 'user_{0}/{1}'.format(self.id, filename)


# Create contact
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50,validators =[validate_geeks_mail])
    mobile = models.CharField(max_length=20, default='00') # when adding a new field into a model set the default value
    address = models.CharField(max_length=200)
    somthing_else = models.TextField()
    date = models.DateField()
    #image= models.ImageField(upload_to="contacts/images", default="")


    def __str__(self):
     return self.email

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(required=False)
    mobile = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    somthing_else = serializers.CharField(required=False)
    date = serializers.CharField(required=False)
    

    def create(self, validated_data):
        """
        Create and return a new `Contact` instance, given the validated data.
        """
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Contact` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.language = validated_data.get('language', instance.language)
        instance.address = validated_data.get('address', instance.address)
        instance.somthing_else = validated_data.get('somthing_else', instance.somthing_else)
        instance.date = validated_data.get('date', models.DateField())
        instance.save()
        return instance


# Create customer item
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20, null=True , blank=True) # when adding a new field into a model set the default value
    customer_email = models.CharField(max_length=50,validators =[validate_geeks_mail])
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    date = models.DateField()
    image= models.ImageField(upload_to="customers/images", default="")

    def __str__(self):
     return self.first_name


# {
#  	"first_name": "22july_sonutyagi.1126@gmail.com",
#     "last_name": "22july_sonutyagi.1126@gmail.com",
#  	"customer_email": "4",
#  	"city": "postman desc from postman id 4 ",
#      "state": "postman desc from postman id 4 ",
#      "zip": "postman desc from postman id 4 ",
#  	"date": "2021-12-31"
#  }

class Musician(models.Model):
    InstrumentType = models.TextChoices('Instrument', 'Guitar Violin Drums')
    musicians_list  = (
        ('Ustad Bismillah', 'Ustad Bismillah'),
        ('R.D. Burman', 'R.D. Burman'),
        ('ARR', 'AR Rahman'),
    )
    first_name = models.CharField(max_length=50, choices=musicians_list)
    last_name = models.CharField(max_length=50, null=True , blank=True,choices=InstrumentType.choices)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
     return self.first_name +" "+self.instrument

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
     return self.name  +"_"+self.artist.first_name




# Many-to-one relationships
#For example, if a Car model has a Manufacturer – that is, a Manufacturer makes multiple cars but each Car only has one Manufacturer – use the following definitions:


class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)



#Many-to-many relationships¶
#For example, if a Pizza has multiple Topping objects – that is, a Topping can be on multiple pizzas and each Pizza has multiple toppings – here’s how you’d represent that:


class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)



class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)





# Create contact
class Plant(models.Model):#https://greatist.com/health/types-of-indoor-plants#small-indoor-plants
    plants_name  = (
        ('Money tree (Pachira aquatica)', 'Money tree (Pachira aquatica)'),
        ('Fiddle leaf fig (Ficus lyrata)', 'Fiddle leaf fig (Ficus lyrata)'),
        ('Rubber plant (Ficus elastica)', 'Rubber plant (Ficus elastica)'),#
        ('Giant bird of paradise (Strelitzia nicolai)', 'Giant bird of paradise (Strelitzia nicolai)'),
        ('Monstera (Monstera deliciosa)', 'Monstera (Monstera deliciosa)')
    )
    availablety  = (('Yes', 'Yes'),('No', 'No'))
    indoor_outdoor  = (('Indoor', 'Indoor'),('Outdoor', 'Outdoor'),('B', 'Both'))
    plant_category = models.CharField(max_length=50, choices=indoor_outdoor)
    id = models.AutoField(primary_key=True)
    plant_name = models.CharField(max_length=50, choices=plants_name, default="")
    plant_available = models.CharField(max_length=50, choices=availablety, default="No")
    plant_subcategory = models.CharField(max_length=50, choices=indoor_outdoor)
    plant_age = models.CharField(max_length=200)
    plant_desc = models.CharField(max_length=500, default="")
    plant_price= models.DecimalField(max_digits=10, decimal_places=2, default="")
    plant_discount_price= models.DecimalField(max_digits=10, decimal_places=2, default="0.0")
    plant_stars = models.IntegerField( default="0")
    date = models.DateField()
    plant_image= models.ImageField(upload_to="plants/images", default="")


    def __str__(self):
     return self.plant_name+"_"+self.plant_category+"_"+str(self.id)

#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver