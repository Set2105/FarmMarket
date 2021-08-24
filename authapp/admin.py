from django.contrib import admin
from .models import CustomerUser, Address

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Address)
