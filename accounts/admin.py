from django.contrib import admin

# Register your models here.
from .models import User, Employee, Customer

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)