from django.shortcuts import render

# Create your views here.


def searchPhotographers(request):
    return render(request, 'search.html')
