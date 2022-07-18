from operator import mod
from django.db import models
from django.forms import ValidationError
from flask import Response
from itsdangerous import Serializer



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
    email = models.CharField(max_length=50,validators =[validate_geeks_mail])
    mobile = models.CharField(max_length=20, default='00') # when adding a new field into a model set the default value
    address = models.CharField(max_length=200)
    somthing_else = models.TextField()
    date = models.DateField()
    image= models.ImageField(upload_to="contacts/images", default="")


    def __str__(self):
     return self.email


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
#python manage.py makemigrations
#python manage.py migrate