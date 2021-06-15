from django.db.models.fields import EmailField
from django.shortcuts import render
from .models import Photographer, Client
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        if(request.POST.get('account_type') == 'Photographer account'):
            # print(request.POST)
            try:
                obj = Photographer.objects.get(email=request.POST.get('email'))
            except Photographer.DoesNotExist:
                Photographer.objects.create(first_name=request.POST.get('first_name'), middle_name=request.POST.get('middle_name'), last_name=request.POST.get('last_name'),
                                            dob=request.POST.get('dob'), country_of_origin=request.POST.get('country_of_origin'), email=request.POST.get('email'), gender=request.POST.get('gender'), username=request.POST.get('username'),
                                            password=request.POST.get('password'), address1=request.POST.get('address1'), address2=request.POST.get('address2'), city=request.POST.get('city'), state=request.POST.get('state'),
                                            zip=request.POST.get('zip'), telephone=request.POST.get('telephone'), member_organization=request.POST.get('member_organization'), base_price=request.POST.get('base_price'))
                context = {
                    'success_message': 'User Successfully registered. Proceed to Login'}
                return render(request, 'registration.html', context)
            context = {
                'error_message': 'Photographer email already exists.'}
            return render(request, 'registration.html', context)
        else:
            # print(request.POST)
            try:
                obj = Client.objects.get(email=request.POST.get('email'))
            except Client.DoesNotExist:
                Client.objects.create(first_name=request.POST.get('first_name'), middle_name=request.POST.get('middle_name'), last_name=request.POST.get('last_name'),
                                      dob=request.POST.get('dob'), country_of_origin=request.POST.get('country_of_origin'), email=request.POST.get('email'), gender=request.POST.get('gender'), username=request.POST.get('username'),
                                      password=request.POST.get('password'), address1=request.POST.get('address1'), address2=request.POST.get('address2'), city=request.POST.get('city'), state=request.POST.get('state'),
                                      zip=request.POST.get('zip'), telephone=request.POST.get('telephone'), member_organization=request.POST.get('member_organization'))
                context = {
                    'success_message': 'User successfully registered. Proceed to Login'}
                return render(request, 'registration.html', context)
            context = {
                'error_message': 'Client email already exists.'}
            return render(request, 'registration.html', context)

    return render(request, 'registration.html')
