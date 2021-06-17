from backend.models import PhotoshootSession
from django.contrib.auth import authenticate, login
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from backend.models import Photographer, Client
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def userlogin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            print(request.POST)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'err_message': 'Invalid Client credentials'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        if(request.POST.get('account_type') == 'Photographer account'):
            # print(request.POST)
            try:
                obj = Photographer.objects.get(Q(email=request.POST.get(
                    'email')) | Q(username=request.POST.get('username')))
            except Photographer.DoesNotExist:
                Photographer.objects.create(first_name=request.POST.get('first_name'), middle_name=request.POST.get('middle_name'), last_name=request.POST.get('last_name'),
                                            dob=request.POST.get('dob'), country_of_origin=request.POST.get('country_of_origin'), email=request.POST.get('email'), gender=request.POST.get('gender'), username=request.POST.get('username'),
                                            password=request.POST.get('password'), address1=request.POST.get('address1'), address2=request.POST.get('address2'), city=request.POST.get('city'), state=request.POST.get('state'),
                                            zip=request.POST.get('zip'), telephone=request.POST.get('telephone'), member_organization=request.POST.get('member_organization'), base_price=request.POST.get('base_price'))

                context = {
                    'success_message': 'User Successfully registered. Proceed to Login'}
                return render(request, 'registration.html', context)
            context = {
                'error_message': 'Photographer email or username already exists.'}
            return render(request, 'registration.html', context)
        else:
            # print(request.POST)
            try:
                obj = User.objects.get(Q(email=request.POST.get('email')) | Q(
                    username=request.POST.get('username')))
            except User.DoesNotExist:
                Client.objects.create(first_name=request.POST.get('first_name'), middle_name=request.POST.get('middle_name'), last_name=request.POST.get('last_name'),
                                      dob=request.POST.get('dob'), country_of_origin=request.POST.get('country_of_origin'), email=request.POST.get('email'), gender=request.POST.get('gender'), username=request.POST.get('username'),
                                      password=request.POST.get('password'), address1=request.POST.get('address1'), address2=request.POST.get('address2'), city=request.POST.get('city'), state=request.POST.get('state'),
                                      zip=request.POST.get('zip'), telephone=request.POST.get('telephone'), member_organization=request.POST.get('member_organization'))
                User.objects.create_user(username=request.POST.get(
                    'username'), email=request.POST.get('email'), password=request.POST.get('password'))
                context = {
                    'success_message': 'User successfully registered. Proceed to Login'}
                return render(request, 'registration.html', context)
            context = {
                'error_message': 'User email or username already exists.'}
            return render(request, 'registration.html', context)

    return render(request, 'registration.html')
