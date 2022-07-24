from django.contrib import admin
from home.models import Album, Car, Contact, Customer, Manufacturer, Membership, Musician, Person, Pizza, Topping,Group,Plant
# Register your models here.
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Plant)

