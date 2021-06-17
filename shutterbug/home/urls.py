from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about', views.about, name='about'),
    path('login', views.userlogin, name='login'),
    path('signup', views.signup, name='signup')
]
