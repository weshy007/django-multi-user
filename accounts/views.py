from django.shortcuts import render
from django.views.generic import CreateView
from .models import User, Customer, Employee
from .forms import CustomerSignUpForm, EmployeeSignUpForm


# Create your views here.
def register(request):
    return render(request, 'register.html')


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_register.html'

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_register.html'