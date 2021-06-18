from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.searchPhotographers, name='search'),
    path('/book', views.book, name='book')
]
